# NoSQL Hands-on Learning

Live-coded for the Clean Coders software engineering book club for a hands-on demonstration of how easy it is to get up and running with modern NoSQL databases, showing basic usage of different NoSQL database types.

## Installation

1. Clone

    ```sh
    git clone https://github.com/camball/nosql-learning
    ```

2. Install dependencies (ensure you have [Python ^3.13](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/docs/#installation) installed on your machine)

    ```sh
    poetry install
    ```

## MongoDB (Document Store)

1. Install MongoDB

    ```sh
    brew tap mongodb/brew
    brew update
    brew install mongodb-community@8.0
    ```

2. Start a local instance of MongoDB in the background

    ```sh
    brew services start mongodb-community@8.0
    ```

> [!TIP]
> With the above command, MongoDB will stay running on the machine until it is manually stopped—even across system reboots. You can stop the service with `brew services stop mongodb-community`.

<!-- markdownlint-disable-next-line ol-prefix -- necessary for GH alert formatting -->
3. Add documents to MongoDB and query for them

    ```sh
    poetry run mongo
    ```

## Redis (Key-value Store)

1. Install Redis

    ```sh
    brew install redis
    ```

2. Start a local instance of Redis in the background

    ```sh
    brew services start redis
    ```

> [!TIP]
> Like our MongoDB instance, starting Redis this way will stay running on the machine until it is manually stopped, and can be stopped with `brew services stop redis`.

<!-- markdownlint-disable-next-line ol-prefix -- necessary for GH alert formatting -->
3. Store a key/value pair in Redis and retrieve that key's value

    ```sh
    poetry run redis
    ```
