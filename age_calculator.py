import datetime

def agecalculate():
   print("-"*40)
   print("AGE CALCULATOR".center(40))
   print("-"*40)
   print("")
   try:
        dobday=int(input("Enter your birth day: "))
        dobmonth=int(input("Enter your birth month: "))
        dobyear=int(input("Enter your birth year: "))
   except ValueError:
        print("Enter valid Birth Credentials.")
   else:
        today=datetime.date.today()
        daycalculate=today.day-dobday
        monthcalculate=today.month-dobmonth
        yearcalculate=today.year-dobyear
        if daycalculate<0:
          monthcalculate-=1
          daycalculate+=30


        if monthcalculate<0:
          yearcalculate-=1
          monthcalculate+=12

        if yearcalculate<0:
          print("Invalid birth year.")
        else:
          print(f"Your age is {yearcalculate} years - {monthcalculate} month - {daycalculate} days ")
agecalculate()
