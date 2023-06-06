import pandas as pd


def query_table(start_date, end_date,table_name,conn_engine):
    """Executes a sql pull on given the date range"""
    print(f'Reading from {table_name} table... ',end='')
    df = pd.read_sql(f"SELECT * FROM {table_name} WHERE date BETWEEN '{start_date}' AND '{end_date}' ", con= conn_engine)
    print('done.')
    return df