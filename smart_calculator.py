import math

def squareroot(n):
  if n<0:
    print("Complex square root.")
  else:
    print(f"Squareroot {n} :{math.sqrt(n)}")

def add(n,m):
  print("Addition : ",n+m)

def sub(n,m):
  print("Subtraction: ",n-m)

def multiply(n,m):
  print("Multiplication: ",n*m)

def division(n,m):
  print("Division: ",n/m)

def factorial(n):
  if n<0:
    print("Factorial not defined for negative number.")
  else:
   print(f"Factorial  {n} :{math.factorial(n)}")

def pow(n):
  a=math.pow(n,2)
  print(f"Power {n}^2 : {a}")

def expo(n):
    print(f"Exponential (e^{n}): {math.exp(n)}")

def log(n):
  if n <= 0:
    print("Logarithm is only defined for positive numbers.")
  else:
    print(f"Base 10 Log (log10 {n}): {math.log10(n)}")

while True:

    print("-"*80)
    print("SMART CALCULATOR".center(80))
    print("-"*80)
    print(" 1. ENTER 1 FOR SQUAREROOT.    ".center(80))
    print(" 2. ENTER 2 FOR ADDITION.      ".center(80))
    print(" 3. ENTER 3 FOR SUBTRACTION.   ".center(80))
    print(" 4. ENTER 4 FOR MULTIPLICATION.".center(80))
    print(" 5. ENTER 5 FOR DIVISION.      ".center(80))
    print(" 6. ENTER 6 FOR FACTORIAL.     ".center(80))
    print(" 7. ENTER 7 FOR POWER.         ".center(80))
    print(" 8. ENTER 8 For EXPONENTIAL.   ".center(80))
    print(" 9. ENTER 9 FOR LOG.           ".center(80))
    print("10. ENTER 10 TO EXIT.           ".center(80))

    print("-"*80 )


    try:
      choice=int(input("\nEnter choice from 1-7: "))
    except ValueError:
      print("Enter valid choice.")
      continue
    if choice==1:
      print("")
      print(("*"*20).center(80))
      print("SQUAREROOT".center(80))
      print(("*"*20).center(80))
      print("")
      try:
        num=int(input("Enter number: "))
      except ValueError:
        print("Invalid Input.")
      else:
        squareroot(num)

    elif choice in [2,3,4,5]:
      try:
        num1=int(input("\nEnter 1st number: "))
        num2=int(input("Enter 2nd number: "))
      except:
        print("Enter valid numbers.")

      if choice==2:
        print("")
        print(("*"*20).center(80))
        print("ADDITION".center(80))
        print(("*"*20).center(80))
        print("")
        add(num1,num2)

      elif choice==3:
        print("")
        print(("*"*20).center(80))
        print("SUBTRACTION".center(80))
        print(("*"*20).center(80))
        print("")
        sub(num1,num2)

      elif choice==4:
        print("")
        print(("*"*20).center(80))
        print("MULTIPLICATION".center(80))
        print(("*"*20).center(80))
        print("")
        multiply(num1,num2)

      elif choice==5:
        print("")
        print(("*"*20).center(80))
        print("DIVISION".center(80))
        print(("*"*20).center(80))
        print("")
        division(num1,num2)

    elif choice==6:
      print("")
      print(("*"*20).center(80))
      print("FACTORIAL".center(80))
      print(("*"*20).center(80))
      print("")

      try:
        num=int(input("Enter number: "))
      except ValueError:
        print("Invalid Input.")
      else:
        factorial(num)

    elif choice==7:
      print("")
      print(("*"*20).center(80))
      print("POWER".center(80))
      print(("*"*20).center(80))
      print("")

      try:
        num=int(input("Enter number: "))
      except ValueError:
        print("Invalid Input.")
      else:
        pow(num)

    elif choice==8:
      print("")
      print(("*"*20).center(80))
      print("EXPONENTIAL".center(80))
      print(("*"*20).center(80))
      print("")

      try:
        num=int(input("Enter number: "))
      except ValueError:
        print("Invalid Input.")
      else:
        expo(num)
    
    elif choice==9:
      print("")
      print(("*"*20).center(80))
      print("LOG".center(80))
      print(("*"*20).center(80))
      print("")

      try:
        num=int(input("Enter number: "))
      except ValueError:
        print("Invalid Input.")
      else:
        log(num)

    elif choice ==10:
      print("")
      print("-"*80)
      print("EXITING SMART CALCULATOR.".center(80))
      print("-"*80)
      break

    else:
      print("Enter valid choice.")
