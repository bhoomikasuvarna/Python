import os
while True:
  print("\n1.Present Directory\n2.Create Directory\n3.Change Directory\n4.Create Text File\n5.List Contents\n6.Remove file\n7.Exit from current directory\n8.Remove Directory\n0.Exit\nEnter any choice : ")
  c=int(input())
  if c==1:
    print("Your Directory is : ",os.getcwd())
  elif c==2:
    dirname=input("Enter name to Directory : ")
    try:
      os.mkdir(dirname)
      print("Directory Created")
    except:
      print("Directory already exist")
  elif c==3:
    direname=input("Enter Directory Name : ")
    try:
      os.chdir(direname)
      print("Directory changed")
    except:
      print("Directory not Exists")


  elif c==4:
    filename=input("Enter file name : ")
    try:
      with open(filename,'w') as f:                       
        f.write("Hello World!")
        print("file created")
    except:
      print("File already Exist ")
  elif c==5:
    print("Contents of Directory",os.listdir())
  elif c==6:
    file=input("Enter file to delete : ")
    try:
      os.remove(file)
      print("File Deleted ")
    except:
      print("File not found ")
  elif c==7:
    try:
      os.chdir("..")
      print("Directory changed")
    except:
      print("Can't change ")
  elif c==8:
    dname=input("Enter Directory name : ")
    try:
      os.rmdir(dname)
      print("Directory deleted")
    except:
      print("Directory not found")
  elif c==0:
    break




