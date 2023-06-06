import pandas as pd

def clean_ticket_replies(replies_df):
    """Cleans ticket replies table.""" 
    print('Cleaning ticket replies table... ', end='')
    # Casts tid as string, removes white space if needed
    replies_df['tid'] = replies_df['tid'].astype('str')
    replies_df = replies_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Get only the first reply for each ticket, rename columns and clean up (select only 4 columns) before merge 
    firstreplies = replies_df.groupby('tid').first()
    first_replies_cleaned = firstreplies.rename(columns={'id':'replyid','date':'firstreplydate','message':'firstreplymsg','admin':'firstreplyadmin','rating':'firstreplyrating'})
    first_response_df = first_replies_cleaned[['replyid','firstreplydate','firstreplymsg','firstreplyadmin']]

    print('done.')
    return first_response_df

def clean_tickets(tickets_df):
    """Clean main  ticket table"""
    print('Cleaning ticket table... ', end='')
    tickets_df['id'] = tickets_df['id'].astype('str')
    tickets_df = tickets_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    print('done.')
    return tickets_df

def clean_departments(departments_df): 
    """Clean departments table"""
    print('Cleaning department table... ', end='')
    departments_df = departments_df[['id','name']]
    departments_df = departments_df.rename(columns={'id':'deptid','name':'department'})
    print('done.')
    return departments_df
