import sqlite3


class DBConnection:

    def __init__(self, instrument):
        """Creates a connection to the database and the table specified by the instrument."""
        self._table = instrument
        self._db = f"./data/historical_prices.db"
        self._conn = sqlite3.connect(self._db)

    @property
    def table(self):
        """Returns the table name of this DBConnection object."""
        return self._table

    @property
    def connection(self):
        """Returns the connection of this DBConnection object."""
        return self._conn
