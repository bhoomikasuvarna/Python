while True:
    print("\nMENU")
    print("1. To open a file")
    print("2. To Append the contents to the file")
    print("3. To search a particular content in file")
    print("4. To replace a particular content in file")
    print("5. Exit")
    ch = int(input("\nEnter your choice "))
   
    if ch == 1:
        a=str(input("Enter the name of the file with .txt extension:"))
        file2=open(a,'r')
        line=file2.readline()
        while(line!=""):
            print(line)
            line=file2.readline()
        file2.close()
       
    elif ch == 2:
        fname = input("Enter file name: ")
        file3=open(fname,"a")
        c=input("Enter string to append: \n");
        file3.write("\n")
        file3.write(c)
        file3.close()
        print("Contents of appended file:");
        file4=open(fname,'r')
        line1=file4.readline()
        while(line1!=""):
            print(line1)
            line1=file4.readline()    
        file4.close()
    elif ch==3:
        fname = input("Enter file name: ")
        word=input("Enter word to be searched:")
        num_words = 0
        with open(fname, 'r') as fp:
                        # read all lines using readline()
            lines = fp.readlines()
            for row in lines:
                                                       
                                # if found it returns index of the first occurrence of the substring
                if row.find(word) != -1:
                    print('string exists in file')
                    print('line Number:', lines.index(row)+1)
    elif ch == 4:
        # Importing FileInput from fileinput module
            from fileinput import FileInput


            # Creating a function to
            # replace the text
            def replacetext(search_text, replace_text):


                # Opening file using FileInput
                with FileInput(fname, inplace=True, backup='.bak') as f:


                    # Iterating over every and changing
                    # the search_text with replace_text
                    # using the replace function
                    for line in f:
                        print(line.replace(search_text,replace_text), end='')


                # Return "Text replaced" string
                return "Text replaced"




            # Creating a variable and storing
            # the text that we want to search
            fname = input("Enter file name: ")
            search_text=input("Enter word to be searched:")
             


            # Creating a variable and storing
            # the text that we want to update
            replace_text =input("Enter word to be replaced:")


            # Calling the replacetext function
            # and printing the returned statement
            print(replacetext(search_text, replace_text))


    elif ch == 5:
        print("Thank You! See you again.")
        break
    else:
        print("Incorrect Choice. Please, try again.")




