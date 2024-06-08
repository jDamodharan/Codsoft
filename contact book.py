import sys

contacts = []

def show_menu():
    print("\nContact Book Application")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def view_contacts():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        print(f"Contact '{name}' added.")
    else:
        print("Name and Phone are required fields.")

def search_contact():
    query = input("Enter name or phone to search: ").lower()
    found_contacts = [contact for contact in contacts if query in contact["Name"].lower() or query in contact["Phone"]]
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
    else:
        print("No matching contacts found.")

def update_contact():
    view_contacts()
    if contacts:
        try:
            contact_number = int(input("Enter the contact number to update: "))
            if 1 <= contact_number <= len(contacts):
                name = input("Enter new name: ")
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contacts[contact_number - 1] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
                print(f"Contact {contact_number} updated.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def delete_contact():
    view_contacts()
    if contacts:
        try:
            contact_number = int(input("Enter the contact number to delete: "))
            if 1 <= contact_number <= len(contacts):
                deleted_contact = contacts.pop(contact_number - 1)
                print(f"Contact '{deleted_contact['Name']}' deleted.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book application.")
            sys.exit()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
