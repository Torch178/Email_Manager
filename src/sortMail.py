from validation_functions import check_token
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail messages.
    """
    creds = check_token()

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = (
            service.users().messages().list(userId="me", labelIds=["INBOX"]).execute()
        )
        messages = results.get("messages", [])

        #parse sender
        for message in messages:
            msg = (
                service.users().messages().get(userId="me", id=message["id"]).execute()
            )
            payload = msg["payload"]
            headers = payload["headers"]
            for data in headers:
                if data["name"] == 'From':
                    print(f"Sender Address: {data["value"]}")



        if not messages:
            print("No messages found.")
            return

        # print("Messages:")
        # for message in messages:
        #     print(f'Message ID: {message["id"]}')
        #     msg = (
        #         service.users().messages().get(userId="me", id=message["id"]).execute()
        #     )
        #     print(f'  Subject: {msg["snippet"]}')

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()