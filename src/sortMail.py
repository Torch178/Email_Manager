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
        results2 = (
            service.users().labels().list(userId="me").execute()
        )
        messages = results.get("messages", [])
        labels = results2.get("labels", [])
        print("Labels:", labels)
        #parse sender
        for message in messages:
            msg = (
                service.users().messages().get(userId="me", id=message["id"]).execute()
            )
            payload = msg["payload"]
            headers = payload["headers"]

            for data in headers:
                if(data["name"] == 'Subject'):
                    subject = data["value"].strip().lower()
                    #if("receipt" in subject or "paid" in subject or "transaction details" in subject or "payment summary" ):







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