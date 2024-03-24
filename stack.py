class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty!")


    def is_empty(self):
        return len(self.items) == 0


    def display(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty!")
stack = Stack()


while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")


    choice = input("Enter your choice (1/2/3/4): ")


    if choice == '1':
        item = input("Enter item to push: ")
        stack.push(item)
    elif choice == '2':
        popped_item = stack.pop()
        if popped_item:
            print("Popped item:", popped_item)
    elif choice == '3':
        stack.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
