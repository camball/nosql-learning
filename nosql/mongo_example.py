from pymongo import MongoClient

# Recall that MongoDB stores BSON technically, so we need to
# use its BSON utils instead of the standard json module
from bson import json_util


def main():
    # Connect to the local MongoDB instance
    client = MongoClient("mongodb://localhost:27017/")

    # Create the db
    db = client["library"]

    # Create or access a collection
    collection = db["books"]

    # Sample document
    book = {
        "title": "How to be a Baller",
        "author": "Branden Evangelista",
        "genres": ["sci-fi", "non-fiction"],
        "page_count": 534,
        "toc": {
            "Intro": 1,
            "What is a Baller?": 5,
            "Since I was Young...": 457,
            "Closing Thoughts": 500,
        },
    }

    # Add the book to the store
    collection.insert_one(book)

    # Another piece of sample data with only a subset of the fields of the first book
    incomplete_book = {
        "title": "How to be a Baller",
        "author": "Branden Evangelista",
    }

    # Add our book with only a subset of the first book's data to the store
    collection.insert_one(incomplete_book)

    # Find all documents by author
    documents = collection.find({"author": "Branden Evangelista"})

    # View our results
    for document in documents:
        print(json_util.dumps(document, sort_keys=True, indent=4), end="\n" * 3)
