from validation_functions import check_token
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from display_functions import *
from helper_functions import get_label_id
from constants import color_keys

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]



def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail messages.
    """
    creds = check_token()

    try:
        #variable declaration
        menu_selection = None
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = (
            service.users().messages().list(userId="me", labelIds=["INBOX"]).execute()
        )
        messages = results.get("messages", [])
        header_params = ["Subject", "From", "To", "Message-ID", "Date"]
        #Main menu
        while(True):
            display_main_menu()
            selection = int(input("Select an option: "))
            match selection:
                case 1:
                    print("Displaying messages...")
                    for message in messages:
                        msg_mata_data = service.users().messages().get(userId='me', id=message['id'], format='metadata', metadataHeaders=header_params).execute()
                        print(msg_mata_data)
                        display_message(msg_mata_data, service)
                    continue
                case 2:
                    print("Displaying Labels...")
                    continue
                case 3:
                    print("Creating Label...")
                    continue
                case 0:
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid selection.")
                    continue


    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()



