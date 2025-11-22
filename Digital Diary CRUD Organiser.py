# Digital Diary CRUD Organiser

diary = {}   # Dictionary to store entries: {date: note}


# 1. CREATE FUNCTION
def create_entry(date, note):
    if date in diary:
        print("Entry already exists for this date!")
    else:
        diary[date] = note
        print("Entry added successfully.")


# 2. READ FUNCTION
def read_entries():
    if not diary:
        print("Diary is empty.")
    else:
        print("\n--- Diary Entries ---")
        for date, note in diary.items():
            print(f"{date}: {note}")
        print("---------------------\n")


# 3. UPDATE FUNCTION
def update_entry(date, new_note):
    if date in diary:
        diary[date] = new_note
        print("Entry updated successfully.")
    else:
        print("No entry found for this date.")


# 4. DELETE FUNCTION
def delete_entry(date):
    if date in diary:
        del diary[date]
        print("Entry deleted successfully.")
    else:
        print("No entry found for this date.")


# MAIN PROGRAM LOOP
while True:
    print("\nDigital Diary CRUD Organiser")
    print("1. Create Entry")
    print("2. Read All Entries")
    print("3. Update Entry")
    print("4. Delete Entry")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        note = input("Enter note: ")
        create_entry(date, note)

    elif choice == "2":
        read_entries()

    elif choice == "3":
        date = input("Enter the date to update: ")
        new_note = input("Enter new note: ")
        update_entry(date, new_note)

    elif choice == "4":
        date = input("Enter the date to delete: ")
        delete_entry(date)

    elif choice == "5":
        print("Exiting Diary... Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")