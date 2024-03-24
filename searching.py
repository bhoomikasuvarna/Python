def linearSearch(list, element):
    for i in range(0, len(list), 1):
        if list[i].lower() == element.lower():
            return i
    return -1


def binarySearch(list, element):

    low = 0
    high = len(names) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if (list[mid] == element):
            return mid
        if (list[mid] > element):
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    num = int(input('\nEnter the number of students: '))
    print('Enter the names of students:')
    names = []
    for i in range(0, num, 1):
        names.append(input('{}: '.format(i+1)))


    choice = 'y'
    while choice.lower() == 'y':
        name=input("\n enter a name to search:")
        print('\n-------- Menu --------')
        print('1. linear search')
        print('2. binary search')
        choice = input('Your Choice: ')
        if choice == '1':
            
            index = linearSearch(names,name)
        elif choice == '2':
            
            index = binarySearch(names,name)
        else:
            print('Invalid Choice!')
        if index == -1:
            print('Name is not in the list.')
        else:
            print('Name found in the list.')
            choice = input('\nWould you like to continue? (y/n): ')


