from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_email_month ():
    month = ''
    #TODO extract month from email

    return month


def get_email_year ():
    year = ''
    # TODO extract year from email
    return year

def get_email_month_year ():
    month = get_email_month()
    year = get_email_year()
    results = [month, year]

    return results