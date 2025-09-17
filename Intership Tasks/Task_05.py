# Contact Management System in Python

contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

# Function to search contact
def search_contact():
    keyword = input("Enter name or phone number to search: ").strip()
    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print("\n✅ Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("❌ Contact not found.\n")

# Function to update contact
def update_contact():
    search_name = input("Enter the name of the contact to update: ").strip()
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("Leave blank if you don't want to update a field.")
            new_name = input("Enter new name: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email: ").strip()
            new_address = input("Enter new address: ").strip()

            if new_name: contact["name"] = new_name
            if new_phone: contact["phone"] = new_phone
            if new_email: contact["email"] = new_email
            if new_address: contact["address"] = new_address

            print("✅ Contact updated successfully!\n")
            return
    print("❌ Contact not found.\n")

# Function to delete contact
def delete_contact():
    search_name = input("Enter the name of the contact to delete: ").strip()
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            contacts.remove(contact)
            print("✅ Contact deleted successfully!\n")
            return
    print("❌ Contact not found.\n")

# Main program loop
def main():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

# Run the program
main()
