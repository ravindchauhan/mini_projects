student_details={}

print("-"*40)
print("")
print("STUDENT RESULT MANAGEMENT SYSTEM.".center(40))
print("")
print("-"*40)
print("")

while True:
  print("-"*40)
  print("")
  print("Enter 1 for adding datails. ".center(40))
  print("Enter 2 for showing datails.".center(40))
  print("Enter 3 for average.        ".center(40))
  print("Enter 4 for topper.         ".center(40))
  print("Enter 5 to exit.            ".center(40))
  print("")
  print("-"*40)

  choice=int(input("Enter your choice: "))

  if choice==1:
    while True:
      name=input("Enter name of student(or enter ok if you don't want to add): ")

      if name.lower()=="ok":
        break

      mark=float(input("Enter mark of student: "))
      print("")
      student_details[name]=mark
    print("Data added successfully.")

  if choice==2:
    print(f"{"Student ID":<15}{"Student Name":<15}{"Marks":<15}")
    for i,(names,marks) in enumerate(student_details.items()):

      print(f"{i+1:<15}{names:<15}{marks:<15}")


  if choice==3:
    all_marks=student_details.values()

    if len(student_details)>0:
     average=sum(all_marks)/len(all_marks)

    print(f"Average marks are:{average}")

  if choice==4:

    for name,mark in student_details.items():
      maxmarks=max(student_details.values())
      if mark==maxmarks:
        print(f"Topper is {name}")

  if choice==5:
    break
    print("Exiting....")
