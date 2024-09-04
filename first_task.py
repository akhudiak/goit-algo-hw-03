from datetime import datetime, date


def get_days_from_today(date_string):

    today = date.today()
    
    try:
        specified_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError as error:
        return error
    
    days_interval = (specified_date - today).days  # specified_date.toordinal() - today.toordinal()
    
    return days_interval

