# Poetry Pytest Demo

This project demonstrates how to set up and run tests using Poetry and pytest, with a MySQL database running in Docker.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Poetry**
- **Docker**

## Steps to Set Up and Run Tests

### 1. **Run MySQL in Docker**

Start a local MySQL container using the following Docker command:

```bash
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=mysql -e MYSQL_PASSWORD=root -e MYSQL_DATABASE=demo -p 3306:3306 -d mysql:8.4.0-oraclelinux8
```

### 2. **Install Project Dependencies**

```shell
cd poetry-pytest
```

Then, install all the project dependencies defined in pyproject.toml:

```shell
poetry install
```

This will set up the virtual environment and install all necessary dependencies.

### 3. **Activate the Virtual Environment**

Activate the virtual environment created by Poetry:

```shell
poetry shell
```

Now you’re inside the Poetry-managed environment, and you can run Python-related commands within this environment.

### 4. **Run the Tests with pytest**

After activating the virtual environment, you can directly run the tests using pytest. To run the tests in the tests/queries/test_person.py file:

```shell
pytest .\tests\queries\test_person.py
```

If you'd like to run all tests in the project, simply use:

```shell
pytest
```
