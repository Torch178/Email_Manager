from validation_functions import check_token
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from helper_functions import get_label_id, display_main_menu

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
        results2 = (
            service.users().labels().list(userId="me").execute()
        )
        messages = results.get("messages", [])
        labels = results2.get("labels", [])

        #Main menu
        while(True):
            display_main_menu()
            selection = int(input("Select an option: "))
            match selection:
                case 1:
                    print("Display messages")
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