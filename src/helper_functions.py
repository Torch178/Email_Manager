from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from constants import color_keys

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
def get_label_id (creds, name):
    try:
        service = build("gmail", "v1", credentials=creds)
        results = (
            service.users().labels().list(userId="me").execute()
        )

        labels = results.get("labels", [])
        for label in labels:
            if label["name"] == name:
                return label["id"]
            else:
                print(f"Label not found: {name}")
                data = collect_input_new_label()
                create_label(service, data["name"], data["color"])
    except HttpError as err:
        print("HTTP Error fetching label Id: ", err)

def collect_input_new_label():
    name = input("Input Label Name: ")
    color = input(f"Input Label Color: \nColor Options: {color_keys.keys()}\n").lower()
    while color not in color_keys:
        print(f"Color not found: {color}")
        color = input(f"Input Color: \nColor Options: {color_keys.keys()}\n").lower()
    data = {"name": name, "color": color}
    return data

#TODO finish create label function, request name, labelListVisibility, messageListVisibility, optional color arg, and set type to "user"
def create_label (service, name, color= color_keys["white"], type = 'user', labelListVisibility = 'labelShow', messageListVisibility='show'  ):
    label_body = {
        "name": name,
        "labelListVisibility": labelListVisibility,
        "messageListvisibility": messageListVisibility,
        "type": type,
        "color": color
    }
    label = service.users().labels().create(userId="me", body=label_body).execute()
    print(f"Created label: {label['name']}\nLabel Data: {label}")
    return label["id"]

def display_main_menu():
    print("\nMain Menu Options: ")
    print("1 - Display messages")
    print("2 - Display labels")
    print("3 - Create label")
    print("0 - Exit Program")