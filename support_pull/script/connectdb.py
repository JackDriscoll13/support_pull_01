from sqlalchemy import create_engine
from decouple import config 

def connect_to_db():
    """Sets up mysql connection engine using enviorment variables"""
    # Read in envrionment variables 
    user = config('MYSQL_USER')
    password = config('MYSQL_PASSWORD')
    conn = config('MYSQL_CONN_NAME')
    port = config('MYSQL_PORT')
    db = config('MYSQL_DATABASE')

    # Establish connection
    mysql_engine = create_engine(f'mysql://{user}:{password}@{conn}:{port}/{db}')

    # Test connection
    mysql_engine.connect()

    return mysql_engine