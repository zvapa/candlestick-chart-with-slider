import pandas as pd


def get_df_from_table(instrument, db_connection):
    """Given an instrument, returns a pandas dataframe from the relevant table in the database."""

    query = f"""
        SELECT *
        FROM {instrument}
    """

    return pd.read_sql(query, db_connection)


def add_bar_counter(df):
    """Adds a 'bar' count column based on the index which is automatically generating when querying the db."""
    df['bar'] = df.index
