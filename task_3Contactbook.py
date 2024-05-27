import pickle
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return results

    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            self.save_contacts()
            return True
        return False

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_contacts()
            return True
        return False

    def save_contacts(self):
        with open('contacts.pkl', 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_contacts(self):
        try:
            with open('contacts.pkl', 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = []

def get_contact_info():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone, email, address)

def main():
    contact_book = ContactBook()
    contact_book.load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            contact = get_contact_info()
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_term)
            if results:
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No contact found.")

        elif choice == '4':
            contact_book.view_contacts()
            index = int(input("Enter the number of the contact to update: ")) - 1
            new_contact = get_contact_info()
            if contact_book.update_contact(index, new_contact):
                print("Contact updated successfully.")
            else:
                print("Invalid contact number.")

        elif choice == '5':
            contact_book.view_contacts()
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if contact_book.delete_contact(index):
                print("Contact deleted successfully.")
            else:
                print("Invalid contact number.")

        elif choice == '6':
            print("Exiting Contact Book.")
            print("THANK YOU!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
