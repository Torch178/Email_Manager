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

#TODO finish get label by ID (Add create label function call if no label exists)
def get_lable_id (creds, name):
    try:
        service = build("gmail", "v1", credentials=creds)
        results = (
            service.users().labels().list(userId="me").execute()
        )

        labels = results.get("labels", [])
        for label in labels:
            if label["name"] == name:
                return label["id"]

        print("Label not found: ", name)
    except HttpError as err:
        print("HTTP Error fetching label Id: ", err)

#TODO finish create label function, request name, labelListVisibility, messageListVisibility, optional color arg, and set type to "user"
def create_label (creds):
    service = build("labels", "v1", credentials=creds)
    label = service.users().labels().create()