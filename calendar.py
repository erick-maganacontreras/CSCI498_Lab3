# Version 1 - Basic Calendar App

events = []

def add_event():
    title = input("Enter event title: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    recurring = input("Is this a recurring event? (yes/no): ")

    events.append({
        "title": title,
        "date": date,
        "recurring": recurring.lower() == "yes"
    })

    print("Event added successfully!\n")

def delete_event():
    title = input("Enter event title to delete: ")
    global events
    events = [event for event in events if event["title"] != title]
    print("Event deleted (if it existed).\n")

def view_events():
    if not events:
        print("No events found.\n")
    else:
        print("\nYour Events:")
        for event in events:
            recurring_text = " (Recurring)" if event.get("recurring") else ""
            print(f"{event['date']} - {event['title']}{recurring_text}")
        print()

if __name__ == "__main__":
    while True:
        print("1. Add Event")
        print("2. Delete Event")
        print("3. View Events")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            delete_event()
        elif choice == "3":
            view_events()
        elif choice == "4":
            break
        else:
            print("Invalid option.\n")
