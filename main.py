import datetime
year_cr = int(datetime.datetime.today().year)
month_cr = int(datetime.datetime.today().month)
date_cr = int(datetime.datetime.today().day)

year_in = int(input("what is the year you were born ? : "))
month_in = int(input("What is the month you were born ? : "))
date_in = int(input("What is the date you were born ? : "))

x = [1,3,5,7,8,10,12]
y = [4,6,9,11]
z = [2]

if month_in in x:
  date_1 = (31 - date_in) + date_cr
  
elif month_in in y:
  date_1 = (30 - date_in) + date_cr
  
elif month_in in z:
  date_1 = (28 - date_in) + date_cr
  
age_1 = year_cr - year_in - 1
month_1 = (11 - month_in) + month_cr
date_2 = (30 - date_in ) + date_cr



if month_1 >= 12:
  age_1 = age_1 + 1
  month_1 = month_1 - 12
if date_1 >=30:
  month_2 = month_1 + 1
  date_1 = date_2 - 30
else:
  month_2 = month_1

print(   )
print(   )

print( "Age in years  = ", age_1,"Years,", month_2,"months," , date_1 , "days .")

months = (12 * int(age_1)) + month_2
days = (30.435 * int(months)) +  + date_1
days = round(days , 0)

print(  )
print(  )

print("Age in months = " , months, "months" ,"+" ,date_1 , "days")
print( )
print("Age in days = " , int(days), "days . ")




