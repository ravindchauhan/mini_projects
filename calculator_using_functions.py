class Calculator:
  def show(self):
    print("""
      ----- CALCULATOR ----
      1.ENTER 1 FOR ADDITION
      2.ENTER 2 FOR SUBTRACTION
      3.ENTER 3 FOR MULTIPLICATION
      4.ENTER 4 FOR DIVISION
      5.ENTER 5 FOR EXIT""")

  def input(self):
     try:
      self.a=int(input("Enter 1st number:"))
      self.b=int(input("Enter 2nd number:"))
      return True
     except ValueError:
      print("Enter a valid Number.")
      return False
  def add(self):
    return self.a+self.b

  def sub(self):
    return self.a-self.b

  def mul(self):
    return self.a*self.b

  def div(self):
    try:
     return self.a/self.b
    except ZeroDivisionError:
     print("Can't Divide by zero.")
    except ValueError:
     print("Enter Invalid number.")
calc=Calculator()

while True:
    calc.show()
    try:
      user_choice=int(input("Enter your choice from (1-5): "))
    except ValueError:
      print("Enter a valid choice from 1-5.")
      continue
    if user_choice==5:
      print("Exiting Calculator.")
      break
    if calc.input():
    
      if user_choice==1:
        print(f"Addition: {calc.add()}")

      elif user_choice==2:
        print(f"Subtraction: {calc.sub()}")
      elif user_choice==3:
        print(f"Multiplication: {calc.mul()}")
      elif user_choice==4:
        print(f"Division: {calc.div()}")
      
      else:
        print("Invalid choice")
