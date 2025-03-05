import os

def create_file(file):
    """Creates a file if it does not exist."""
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write("")
        print(f"{file} created successfully")
    else:
        print(f"{file} already exists")

def insert_cont(file, contact):
    """Inserts a contact number into the file."""
    with open(file, "a") as f:
        f.write(contact + "\n")
    print(f"{contact} added successfully")
    
def clean_db(file):
    """Removes duplicate entries from the file."""
    with open(file, "r") as f:
        contacts = set(f.readlines())
    
    with open(file, "w") as f:
        f.writelines(contacts)
    print("Database cleaned successfully")

if __name__ == "__main__":  # Corrected condition
    file = input("Enter file name: ").strip() or "contacts.txt"
    create_file(file)
    
    while True:
        number = input("Enter a 10-digit number (or 'exit' to stop): ").strip()

        if number.lower() == "exit":
            print("Exiting program.")
            clean_db(file)
            break  # Exits the loop

        if not number.isdigit() or len(number) != 10:
            print("Invalid input! Please enter a valid 10-digit number.")
            continue

        contact = "+91" + number  # Ensuring correct format
        insert_cont(file, contact)
