# Create an empty dictionary to store the telephone directory
telephone_directory = {}

# Function to add a contact to the directory
def add_contact():
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number: ")
    telephone_directory[name] = number
    print("Contact added successfully!")

# Function to change a contact's data
def change_contact():
    name = input("Enter the name of the contact you want to change: ")
    if name in telephone_directory:
        new_number = input("Enter the new phone number: ")
        telephone_directory[name] = new_number
        print("Contact data changed successfully!")
    else:
        print("Contact not found!")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in telephone_directory:
        del telephone_directory[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Main program loop
while True:
    print("1. Add a contact")
    print("2. Change contact data")
    print("3. Delete a contact")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        change_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Print the updated telephone directory
print("Updated Telephone Directory:")
for name, number in telephone_directory.items():
    print(f"{name}: {number}")