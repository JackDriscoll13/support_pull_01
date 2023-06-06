from dateutil import parser 
from datetime import datetime

def check_dates(start_date,end_date):
    """Validates dates/date range. Prompts repeated user input if incorrect."""
    try: 
        bool(parser.parse(start_date))
        bool(parser.parse(end_date))
        if datetime.strptime(start_date, '%Y-%m-%d').date() > datetime.strptime(end_date, '%Y-%m-%d').date():
            print('Date 1 interpreted as being after date 2, please fix this...')
            raise ValueError
    except Exception as e: 
        print(e)
        print('Dates not specified in script or is  incorrect. Prompting user for date range...')
        while True: 
            try:
                start_date = input('Please input the start date (YYYY-MM-DD): ')
                bool(parser.parse(start_date))
                end_date = input('Please input the end date (YYYY-MM-DD): ')
                bool(parser.parse(end_date))
                if datetime.strptime(start_date, '%Y-%m-%d').date() > datetime.strptime(end_date, '%Y-%m-%d').date():
                    raise ValueError
                break
            except:
                print('improper input, please ensure dates are in YYYY-mm-dd format and the start date is before the end date and try again')
    print(f'Proceeding with data pull. \nDate range: {start_date} - {end_date}') 
    return start_date, end_date