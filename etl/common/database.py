import sqlite3

class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        """Returns the single instance of the database connection."""
        if cls._connection is None:
            cls._connection = sqlite3.connect("data/database/aml.db")
        return cls._connection

    @classmethod
    def close_connection(cls):
        """Safely closes the connection and resets the singleton."""
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
