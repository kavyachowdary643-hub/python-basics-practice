contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Show Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")

        contacts[name] = number
        print("Contact Added")

    elif choice == "2":
        name = input("Enter name: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "3":
        if len(contacts) == 0:
            print("No Contacts")

        else:
            for name, number in contacts.items():
                print(name, ":", number)

    elif choice == "4":
        name = input("Enter contact name: ")

        if name in contacts:
            del contacts[name]
            print("Deleted Successfully")
        else:
            print("Contact Not Found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")