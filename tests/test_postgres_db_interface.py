import os
import pytest
from sqlalchemy import text
from src.postgres_db_interface import PostgresDBInterface

def test_db_connection():
    """
    Tests the connection to the PostgreSQL database.

    :returns: None
    :raises AssertionError: If the connection was not successful
    """
    # Setup: instantiate the PostgresDBInterface class with environment variables
    db_interface = PostgresDBInterface(
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOSTNAME'),
        os.getenv('DB_NAME')
    )

    # Act and Assert: call the connect method and assert successful connection
    try:
        db_interface.connect()
        assert db_interface.engine is not None
    except Exception as e:
        pytest.fail(f"Database connection failed with exception: {e}")

@pytest.mark.parametrize("username,password,hostname,database,expected_exception",
                         [("wrong_username", os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'), True),
                          (os.getenv('DB_USERNAME'), "wrong_password", os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'), True),
                          (os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), "wrong_hostname", os.getenv('DB_NAME'), True),
                          (os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), "wrong_database", True)])
def test_db_connection_failure(username, password, hostname, database, expected_exception):
    """
    Tests the failure of connection to the PostgreSQL database with incorrect credentials.

    :returns: None
    :raises AssertionError: If the connection does not fail as expected
    """
    # Setup: instantiate the PostgresDBInterface class with incorrect credentials
    db_interface = PostgresDBInterface(username, password, hostname, database)

    # Act and Assert: call the connect method and expect failure
    if expected_exception:
        with pytest.raises(Exception):
            db_interface.connect()
    else:
        try:
            db_interface.connect()
        except Exception as e:
            pytest.fail(f"Database connection failed with exception: {e}")


def test_db_create_table():
    """
    Test if we can create a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'))
    db_interface.connect()
    with db_interface.engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_name = 'test_table';"))
        assert result.fetchone()[0] == 'test_table'
        connection.execute(text("DROP TABLE test_table;"))  # cleanup

def test_db_insert():
    """
    Test if we can insert into a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'))
    db_interface.connect()
    with db_interface.engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
        connection.execute(text("INSERT INTO test_table (test_value) VALUES ('test_value');"))
        result = connection.execute(text("SELECT * FROM test_table WHERE test_value = 'test_value';"))
        assert result.fetchone()[1] == 'test_value'
        connection.execute(text("DROP TABLE test_table;"))  # cleanup

def test_db_select():
    """
    Test if we can select from a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'))
    db_interface.connect()
    with db_interface.engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
        connection.execute(text("INSERT INTO test_table (test_value) VALUES ('test_value');"))
        result = connection.execute(text("SELECT * FROM test_table;"))
        assert result.fetchone()[1] == 'test_value'
        connection.execute(text("DROP TABLE test_table;"))  # cleanup

def test_db_update():
    """
    Test if we can update a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'))
    db_interface.connect()
    with db_interface.engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
        connection.execute(text("INSERT INTO test_table (test_value) VALUES ('test_value');"))
        connection.execute(text("UPDATE test_table SET test_value = 'new_test_value' WHERE test_value = 'test_value';"))
        result = connection.execute(text("SELECT * FROM test_table;"))
        assert result.fetchone()[1] == 'new_test_value'
        connection.execute(text("DROP TABLE test_table;"))  # cleanup

def test_db_drop_table():
    """
    Test if we can drop a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'))
    db_interface.connect()
    with db_interface.engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
        connection.execute(text("DROP TABLE test_table;"))
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_name = 'test_table';"))
        assert result.fetchone() is None
