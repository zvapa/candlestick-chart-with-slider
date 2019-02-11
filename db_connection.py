import sqlite3


class DBConnection:

    def __init__(self, path=f"./data/historical_prices.db"):
        """Creates a connection to the database."""

        self._db = path
        self._conn = sqlite3.connect(self._db)

    @property
    def connection(self):
        """Returns the connection of this DBConnection object."""
        return self._conn

    @property
    def tables(self):
        """Returns a list of tables in the database"""
        cursor = self.connection.cursor()
        tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        return [t[0] for t in tables]
