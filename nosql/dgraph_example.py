import pydgraph


def main():
    # Connect to database
    client_stub = pydgraph.DgraphClientStub("localhost:9080")
    client = pydgraph.DgraphClient(client_stub)

    # Define and commit our schema
    schema = "name: string @index(exact) ."
    op = pydgraph.Operation(schema=schema)
    client.alter(op)

    # Add some data (a node)
    txn = client.txn()
    try:
        person = {"uid": "_:person1", "name": "Alice", "age": 25}
        response = txn.mutate(set_obj=person, commit_now=True)
        print("Created person with UID:", response.uids["person1"])
    finally:
        txn.discard()

    # Add some more data (another node)
    txn = client.txn()
    try:
        person = {"uid": "_:person2", "name": "Bob", "age": 26}
        response = txn.mutate(set_obj=person, commit_now=True)
        print("Created person with UID:", response.uids["person2"])
    finally:
        txn.discard()

    print()  # separator

    # Query the database via GraphQL
    query = """
    {
      all(func: has(name)) {
        uid
        name
        age
      }
    }
    """
    response = client.txn(read_only=True).query(query)
    print("Query response:")
    print(response.json)

    # Exercise for the reader:
    #   - Modify the database schema to create a "friend" relationship
    #     (graph edge) between nodes
    #   - Query for all friends of a specific person
