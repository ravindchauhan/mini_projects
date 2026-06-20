class Numbers:

  def displayeven(self):

      b=lambda x:x%2==0

      try:
       self.x=int(input("Enter starting range: "))
       self.y=int(input("Enter ending range: "))
       print("")
      except ValueError:
       print("Enter valid range.")
      print("")
      self.num=filter(b,range(self.x,self.y+1))

      listt=(list(self.num))

      self.c=iter(listt)
      print(("*"*20).center(40))
      print("")
      print(f"EVEN NUMS FROM {self.x} - {self.y}:\n".center(40))
      print(("*"*20).center(40))
      print("")
      for i in range (0,len(listt)):
          print(next(self.c))
      print(f"Count of even numbers: {len(listt)}")

  def displayodd(self):

      b=lambda x:x%2!=0

      try:
       self.x=int(input("Enter starting range: "))
       self.y=int(input("Enter ending range: "))
       print("")
      except ValueError:
       print("Enter valid range.")

      self.num=filter(b,range(self.x,self.y+1))
      listt=(list(self.num))
      self.c=iter(listt)
      print(("*"*20).center(40))
      print(f"ODD NUMS FROM {self.x}-{self.y}:\n".center(40))
      print(("*"*20).center(40))
      print("")
      for i in range (0,len(listt)):
          print(next(self.c))
      print(f"Count of odd Numbers: {len(listt)}")

  def prime_nums(self):
     
     try:
      self.x=int(input("Enter starting range: "))
      self.y=int(input("Enter ending range: "))
      print("")
     except ValueError:
      print("Enter valid range.")
     
     def is_prime(n):
            if n < 2:
                  return False
            for i in range(2, int(n**0.5) + 1):
                  if n % i == 0:
                       return False
            return True
     
     self.num=filter(is_prime,range(self.x,self.y+1))
     listt=(list(self.num))
     self.c=iter(listt)
     print(("*"*20).center(40))
     print("")
     print(f"PRIME NUMS FROM {self.x}-{self.y}:\n".center(40))
     print(("*"*20).center(40))
     print("")
     for i in range (0,len(listt)):
         print(next(self.c))
     print(f"Count of prime Numbers: {len(listt)}")

  def input(self):
    print("-"*40)
    print("EVEN,ODD,PRIME NUMBERS FINDER.".center(40))
    print("-"*40)
    print("")
    print("ENTER 1 FOR EVEN NUMBERS.  ".center(40))
    print("ENTER 2 FOR ODD NUMBERS.   ".center(40))
    print("ENTER 3 FOR PRIME NUMBERS. ".center(40))
    print("")
    print("-"*40)
    print("")
    try:
     self.choice=int(input("Enter your choice: "))
    except ValueError:
      print("Enter valid choice.")
      
    if self.choice==1:

      self.displayeven()
    elif self.choice==2:

      self.displayodd()
    
    elif self.choice==3:
      self.prime_nums()
      
    else:
      print("Enter valid choice.")

numbers=Numbers()
numbers.input()
