def add_key_value(dictionary):
    """Adds a key-value pair to the dictionary"""
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value
    print("Key-value pair added successfully")

def remove_key_value(dictionary):
    """Removes a key-value pair from the dictionary"""
    key = input("Enter key to remove: ")
    if key in dictionary:
        del dictionary[key]
        print("Key-value pair removed successfully")
    else:
        print("Key not found in dictionary")

def access_key_value(dictionary):
    """Accesses a value based on a key in the dictionary"""
    key = input("Enter key to access: ")
    if key in dictionary:
        print(f"Value: {dictionary[key]}")
    else:
        print("Key not found in dictionary")

def display_dictionary(dictionary):
    """Displays all key-value pairs in the dictionary"""
    print("Current Dictionary:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def replace_key(dictionary):
    """Replaces a key in the dictionary"""
    old_key = input("Enter the old key: ")
    if old_key in dictionary:
        new_key = input("Enter the new key: ")
        dictionary[new_key] = dictionary.pop(old_key)
        print("Key replaced successfully")
    else:
        print("Old key not found in dictionary")

def replace_value(dictionary):
    """Replaces a value in the dictionary"""
    key = input("Enter key: ")
    if key in dictionary:
        new_value = input("Enter new value: ")
        dictionary[key] = new_value
        print("Value replaced successfully")
    else:
        print("Key not found in dictionary")
dictionary={}
while True:
    """Displays the menu of options"""
    print("1. Add key-value pair")
    print("2. Remove key-value pair")
    print("3. Access value by key")
    print("4. Display dictionary")
    print("5. Replace key")
    print("6. Replace value")
    print("7. Exit")
    choice= int(input("Enter your choice: "))

    

    if choice == 1:
        add_key_value(dictionary)
    elif choice == 2:
        remove_key_value(dictionary)
    elif choice == 3:
        access_key_value(dictionary)
    elif choice == 4:
        display_dictionary(dictionary)
    elif choice == 5:
        replace_key(dictionary)
    elif choice == 6:
        replace_value(dictionary)
    elif choice == 7:
        break
    else:
        print("Invalid choice")
