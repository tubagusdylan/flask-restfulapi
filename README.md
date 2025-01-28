# Student RestfulAPI

This is a simple API to learn how flask works.

## Installation

1. First you need to create a .venv folder

``` bash
python -m venv venv
source venv/bin/activate # macOS / linux
venv\Scripts\activate    # windows
```

2. Install flask, flask_sqlalchemy, psycopg2, and python_dotenv

``` bash
pip install flask flask_sqlalchemy psycopg2 python_dotenv
```

3. Add <b>.env file</b> on your project, especially for your database url, you can use PostgreSql, or others. You can see the example below.

``` .env
DEV_DATABASE_URI=postgresql://postgres:postgres@localhost:5432/test_db
```
4. Don't forget to create a database on your local computer, and create a table for this simple project. You can use query in <b>database.sql</b> file.

5. You are ready to run this project.

## Running the project

To run the project, just type the command below on your terminal.

``` bash
python run.py
```
