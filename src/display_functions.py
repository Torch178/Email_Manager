from constants import color_keys

def display_main_menu():
    print("\nMain Menu Options: ")
    print("1 - Display messages")
    print("2 - Display labels")
    print("3 - Create label")
    print("0 - Exit Program")

def display_message(message, service):
    #variables
    labels = message.get("labelIds", [])
    payload = message.get("payload", [])
    headers = payload["headers"]
    print(f"Message ID: {message["id"]}")
    print("Labels")

    #TODO display labels for messages. Getting an error when referencing color data
    # for label in labels:
    #     label_data = service.users().labels().get(userId="me", id=label).execute()
    #     print(f"Label ID: {label_data["id"]}\n\tName: {label_data["name"]}\n\tText Color: {color_keys[label_data["color"]["textColor"]]}\tBackground Color: {color_keys[label_data["color"]["backgroundColor"]]}")
    for header in headers:
        print(f"{header["name"]}: - {header["value"]}")

    print("\n---------------------------\n")