""" Solution of Given Programming Exercise ****
Find Largest among 3 Numbers"""

# Take First Number from User
num1= input("Please enter First Number : -  ")
 
# Take Second Number from User
num2= input("Please enter Second Number : -  ")
 
# Take Third Number from User
num3= input("Please enter Third Number : -  ")
 
if(int(num1) >= int(num2) and int(num1) >= int(num3)):
    print(" Largest among 3 is " + num1)
 
elif(int(num2) >= int(num1) and int(num2) >= int(num3)):
    print(" Largest among 3 is " + num2)
else:
    print(" Largest among 3 is " + num3)


Find Lowest among 3 Numbers

# Take First Number from User
num1= input("Please enter First Number : -  ")
 
# Take Second Number from User
num2= input("Please enter Second Number : -  ")
 
# Take Third Number from User
num3= input("Please enter Third Number : -  ")
 
if(int(num1) <= int(num2) and int(num1) <= int(num3)):
    print(" Smallest among 3 is " + num1)
 
elif(int(num2) <= int(num1) and int(num2) <= int(num3)):
    print(" Smallest among 3 is " + num2)
else:
    print(" Smallest among 3 is " + num3)


Check number is Divisible by  5 and 11

# Take input Number from User
num1= input("Please enter your Number : -  ")
 
if(int(num1)%5==0 and int(num1)%11==0):
    print("Number is Divisible by both 5 and 11")
elif(int(num1)%5==0):
    print("Number is Divisible by 5 only")
elif(int(num1)%11==0):
    print("Number is Divisible by 11 only")
else:
    print("Number is Not Divisible by 5 and 11 both")


Check number of days in a Month

# Take input month Number from User
month_number= int(input("Please enter month number : -  "))
 
if(month_number > 0  and month_number <=12):
    if(month_number==2):
        print("Total number of days are : - 28")
    elif(month_number==1 or month_number==3 or month_number==5 or month_number==7 or month_number==8 or month_number==10 or month_number==12 ):
        print("Total number of days are : - 31")
    else:
        print("Total number of days are : - 30")
else:
    print("Your month number is INVALID, Please enter correct month number")
Find triangle -EQUILATERAL|SCALENE|ISOSCELES

# Take input from User - First side length of Triangle
first_side= int(input("Please enter length of first side : -  "))
 
# Take input from User - Second side length of Triangle
second_side= int(input("Please enter length of second side : -  "))
 
 
# Take input from User - Third side length of Triangle
third_side= int(input("Please enter length of third side : -  "))
 
 
if(first_side!=second_side and first_side!=third_side):
    print("This triangle is a SCALENE Triangle")
 
elif(first_side==second_side and first_side==third_side):
    print("This triangle is a EQUILATERAL Triangle")
 
elif(first_side==second_side or first_side==third_side):
    print("This triangle is a ISOSCELES Triangle")


Find Grade by calculating percentage

# Take input from User
maths= int(input("Please enter math marks : -  "))
english= int(input("Please enter english marks : -  "))
physics= int(input("Please enter physics marks : -  "))
chemestry= int(input("Please enter chemestry marks : -  "))
biology= int(input("Please enter biology marks : -  "))
 
average = (maths+english+physics+chemestry+biology)/5
 
if(average>=90):
    print("Your grade is  --  A")
 
elif(average>=80):
    print("Your grade is  --  B")
 
elif(average>=70):
    print("Your grade is  --  C")
 
elif(average>=60):
    print("Your grade is  --  D")
 
elif(average>=50):
    print("Your grade is  --  E")
 
elif(average>=40):
    print("Your grade is  --  F")
else:
    print("No Grade")
Check Number is EVEN OR ODD

#  Take input number from User and check its a EVEN NUMBER or ODD Number
 
input_num = int(input("Please enter your number --- > "))
 
if(input_num%2==0):
    print("This is an even number...")
else:
    print("This is an ODD number...")
Check Number is NEGATIVE, ZERO, EVEN OR ODD



#  Take input number from User and check its a EVEN NUMBER or ODD Number
 
input_num = int(input("Please enter your number --- > "))
 
if(input_num<0):
    print("This is a NEGATIVE number...")
elif(input_num==0):
    print("This is ZERO  number...")
elif(input_num%2==0):
    print("This is an EVEN NUMBER...")
else:
    print("This is an ODD Number")