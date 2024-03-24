def bubbleSort(list):
    for i in range(0, len(list)-1, 1):
        for j in range(0, len(list) - i - 1, 1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


def insertionSort(list):
    for i in range(0, len(list), 1):
        temp = list[i]
        j = i - 1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp
    return list


def selectionSort(list):
    for i in range(0, len(list)-1, 1):
        minIndex = i
        for j in range(i+1, len(list), 1):
            if list[minIndex] > list[j]:
                minIndex = j
        temp = list[minIndex]
        list[minIndex] = list[i]
        list[i] = temp
    return list

if __name__ == "__main__":
    num = int(input('\nEnter the number of students: '))
    print('Enter the names of students:')
    names = []
    for i in range(0, num, 1):
        names.append(input('{}: '.format(i+1)))


    choice = 'y'
    while choice.lower() == 'y':
        print('\n-------- Menu --------')
        print('1. bubble sort')
        print('2. insertion sort')
        print('3. selection sort')
        
        choice = input('Your Choice: ')
        sorted_names = []
        if choice == '1':
            sorted_names = bubbleSort(names)
        elif choice == '2':
            sorted_names = insertionSort(names)
        elif choice == '3':
            sorted_names = selectionSort(names)
        else:
            print('Invalid Choice!') 
        print('Sorted list: ', end='')
        for i in range(0, len(sorted_names), 1):
            print('\'{}\''.format(sorted_names[i]), end=' ')
        print('')
        


        choice = input('\nWould you like to continue? (y/n): ')


