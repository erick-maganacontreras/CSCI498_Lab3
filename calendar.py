# Version 5 - Basic Calendar App
import json
from datetime import datetime
import csv

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

def save_events():
    with open("events.json", "w") as file:
        json.dump(events, file)
    print("Events saved to file.\n")

def load_events():
    global events
    try:
        with open("events.json", "r") as file:
            events = json.load(file)
    except FileNotFoundError:
        events = []

def check_reminders():
    today = datetime.now().strftime("%Y-%m-%d")
    for event in events:
        if event["date"] == today:
            print(f"Reminder: You have '{event['title']}' today!")

def export_to_csv():
    with open("events.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Date", "Recurring"])
        for event in events:
            writer.writerow([
                event["title"],
                event["date"],
                event.get("recurring", False)
            ])
    print("Events exported to CSV.\n")

if __name__ == "__main__":
    load_events()
    check_reminders()
    while True:
        print("1. Add Event")
        print("2. Delete Event")
        print("3. View Events")
        print("4. Exit")
        print("5. Export to CSV")

        choice = input("Choose an option: ")

        if choice == "1":
            add_event()
            save_events()
        elif choice == "2":
            delete_event()
            save_events()
        elif choice == "3":
            view_events()
        elif choice == "4":
            break
        elif choice == "5":
            export_to_csv()
        else:
            print("Invalid option.\n")
