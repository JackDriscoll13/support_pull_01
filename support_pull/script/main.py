import pandas as pd

from .connectdb import connect_to_db
from .date_validation import check_dates
from .select import query_table


def main(): 
    # Option to put start date and end date here
    start_date = ''
    end_date = ''

    # Check for valid start date and end date, require input if not
    start_date, end_date = check_dates(start_date, end_date)
    
    # Connect to my sql
    conn_engine = connect_to_db()
    
    # Pull the tables we need for the dates we want
    tickets = query_table(start_date,end_date,'tbltickets',conn_engine)
    ticketreplies = query_table(start_date,end_date,'tblticketreplies',conn_engine)
    departments = query_table(start_date,end_date,'tblticketdepartments',conn_engine)
    
