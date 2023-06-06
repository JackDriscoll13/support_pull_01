import pandas as pd

from connectdb import connect_to_db
from date_validation import check_dates
from select import query_table
from datacleaning import clean_ticket_replies, clean_tickets, clean_departments

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
    departments = query_table(start_date, end_date, 'tblticketdepartments', conn_engine)
    
    # Clean the three tables
    first_replies_df = clean_ticket_replies(ticketreplies)
    tickets_df = clean_tickets(tickets)
    departments_df = clean_departments(departments)

    # Merge
    print('Merging dataframes... ', end='')
    end_df = tickets_df.merge(first_replies_df, how='left', left_on='id', right_on='tid')
    end_df = end_df.merge(departments_df, how='left', left_on='did',right_on='deptid')
    print('done.')

    # Calculate first response time
    end_df['firstresponsetime'] = (end_df['firstreplydate'] - end_df['date'])

    # Export to csv
    export_path1 = 'outputs/output1.csv'
    export_path2 = 'outputs/output2.csv'

    end_df.to_csv(export_path1)
    end_df[['department','firstresponsetime']].to_csv(export_path2)

    print(f'Script Complete. End results exported to {export_path1} and {export_path2}.')
    return end_df

if __name__ == '__main__':
    main()