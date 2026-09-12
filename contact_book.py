contacts = {}
while True:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Remove contact")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts[name] = phone
        print("Contact added.")
    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)
    elif choice == "3":
        name = input("Enter the contact name to remove: ")
        if name in contacts:
            del contacts[name]
            print("Contact removed.")
        else:
            print("contact not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")