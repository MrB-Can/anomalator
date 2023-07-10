import os
from pprint import pprint
from prettytable import PrettyTable
import pytest
from sqlalchemy import text
from src.database_interface import PostgresDBInterface


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
                         [("wrong_username", os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'),
                           True),
                          (os.getenv('DB_USERNAME'), "wrong_password", os.getenv('DB_HOSTNAME'), os.getenv('DB_NAME'),
                           True),
                          (os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), "wrong_hostname", os.getenv('DB_NAME'),
                           True),
                          (os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'),
                           "wrong_database", True)])
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
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'),
                                       os.getenv('DB_NAME'))
    db_interface.connect()
    db_interface.connection.execute(
        text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
    result = db_interface.connection.execute(
        text("SELECT table_name FROM information_schema.tables WHERE table_name = 'test_table';"))
    assert result.fetchone()[0] == 'test_table'
    db_interface.connection.execute(text("DROP TABLE test_table;"))  # cleanup
    db_interface.disconnect()


def test_db_insert():
    """
    Test if we can insert into a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'),
                                       os.getenv('DB_NAME'))
    db_interface.connect()
    db_interface.connection.execute(
        text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
    db_interface.connection.execute(text("INSERT INTO test_table (test_value) VALUES ('test_value');"))
    result = db_interface.connection.execute(text("SELECT * FROM test_table WHERE test_value = 'test_value';"))
    assert result.fetchone()[1] == 'test_value'
    db_interface.connection.execute(text("DROP TABLE test_table;"))  # cleanup
    db_interface.disconnect()


def test_db_select():
    """
    Test if we can select from a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'),
                                       os.getenv('DB_NAME'))
    db_interface.connect()
    db_interface.connection.execute(
        text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
    db_interface.connection.execute(text("INSERT INTO test_table (test_value) VALUES ('test_value');"))
    result = db_interface.connection.execute(text("SELECT * FROM test_table;"))
    assert result.fetchone()[1] == 'test_value'
    db_interface.connection.execute(text("DROP TABLE test_table;"))  # cleanup
    db_interface.disconnect()


def test_db_update():
    """
    Test if we can update a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'),
                                       os.getenv('DB_NAME'))
    db_interface.connect()
    db_interface.connection.execute(
        text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
    db_interface.connection.execute(text("INSERT INTO test_table (test_value) VALUES ('test_value');"))
    db_interface.connection.execute(
        text("UPDATE test_table SET test_value = 'new_test_value' WHERE test_value = 'test_value';"))
    result = db_interface.connection.execute(text("SELECT * FROM test_table;"))
    assert result.fetchone()[1] == 'new_test_value'
    db_interface.connection.execute(text("DROP TABLE test_table;"))  # cleanup
    db_interface.disconnect()


def test_db_drop_table():
    """
    Test if we can drop a table in the database.
    """
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'),
                                       os.getenv('DB_NAME'))
    db_interface.connect()
    db_interface.connection.execute(
        text("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, test_value VARCHAR(50));"))
    db_interface.connection.execute(text("DROP TABLE test_table;"))
    result = db_interface.connection.execute(
        text("SELECT table_name FROM information_schema.tables WHERE table_name = 'test_table';"))
    assert result.fetchone() is None
    db_interface.disconnect()


def test_db_disconnect():
    """Test that disconnect actually closes the connection"""
    db_interface = PostgresDBInterface(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOSTNAME'),
                                       os.getenv('DB_NAME'))
    db_interface.connect()  # Establish the connection

    # Now disconnect
    db_interface.disconnect()

    # Verify the connection is closed by trying to perform an operation
    with pytest.raises(Exception):
        # Trying to access the closed connection should raise an Exception
        db_interface.connection.execute("SELECT 1")


from prettytable import PrettyTable

def test_database_profiling():
    """
    Test if we can profile the database.
    """
    db_interface = PostgresDBInterface(
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOSTNAME'),
        os.getenv('DB_NAME')
    )
    db_interface.connect()
    db_profile = db_interface.profile_database()
    db_interface.disconnect()

    # Databases table
    db_table = PrettyTable()
    db_table.field_names = ["Database", "Character Encoding", "Collation"]
    for database in db_profile:
        profile_data = db_profile[database]
        db_table.add_row([database, profile_data.get('character_encoding', ''), profile_data.get('collation', '')])

    # Schemas table
    schema_table = PrettyTable()
    schema_table.field_names = ["Database", "Schema"]
    for database in db_profile:
        for schema in db_profile[database]['schemas']:
            schema_table.add_row([database, schema['name']])

    # Tables table
    table_table = PrettyTable()
    table_table.field_names = ["Database", "Schema", "Table", "Row Count"]
    for database in db_profile:
        for schema in db_profile[database]['schemas']:
            for table in schema['tables']:
                table_table.add_row([database, schema['name'], table['name'], table['row_count']])

    # Columns table
    column_table = PrettyTable()
    column_table.field_names = ["Database", "Schema", "Table", "Column", "Data Type", "Is Nullable", "Default",
                                "Min Value", "Max Value"]  # Include "Min Value" and "Max Value" fields
    for database in db_profile:
        for schema in db_profile[database]['schemas']:
            for table in schema['tables']:
                for column in table['columns']:
                    column_table.add_row([
                        database,
                        schema['name'],
                        table['name'],
                        column['name'],
                        column['type'],
                        column['nullable'],
                        column['default'],
                        column.get('min_value', ''),
                        column.get('max_value', '')
                    ])

    # Print tables
    print(db_table)
    print(schema_table)
    print(table_table)
    print(column_table)


