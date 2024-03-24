my_list = []

while True:
    print("1. Create a new list")
    print("2. Add an item to the list")
    print("3. Remove an item from the list")
    print("4. Display the list")
    print("5. exit")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        my_list = []
        print("New list created")

    elif choice == 2:
        item = input("Enter the item to add: ")
        my_list.append(item)
        print(item, "added to the list")

    elif choice == 3:
        if len(my_list) == 0:
            print("The list is empty")
        else:
            item = input("Enter the item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(item, "removed from the list")
            else:
                print(item, "is not in the list")
    elif choice==4:
        print("\nList contents")
        for item in my_list:
            print(item)
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

