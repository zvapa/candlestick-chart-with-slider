import pandas as pd
from db_connection import DBConnection


def get_df(instrument):
    """Given an instrument, returns a pandas dataframe from the relevant table in the database."""
    db = DBConnection(instrument)

    query = f"""
        SELECT *
        FROM {db.table}
    """
    return pd.read_sql(query, db.connection)


def add_bar_counter(df):
    df['bar'] = df.index
