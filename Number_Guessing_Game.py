import random
print("***********  NUMBER GUESSING GAME  ***********")

key=random.randint(0,100)
attempt=0
while(True):
  try:
    guess=int(input("Enter Number From 0-100 : "))
    attempt+=1
  except ValueError:
    print("Enter a whole number.")
    continue

  else:
      if(guess not in range(0,101)):
        print("Enter range between 0 and 100.")
        continue
      if(guess==key):

        print("----✌️You have guessed correct number✌️----")
        print(f"Number of tries you took: {attempt}")
        break

      elif(guess<key):
        print("Try Higher Number..")

      elif(guess>key):
        print("Try Lower Number..")

      else:
        print("Invalid Input..")
