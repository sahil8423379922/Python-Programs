#True and False
#Logical operator is use to combine two or more conditions
# a>b  b>c
# and , or , not
# 2+3 , 5*10

# Logical and
# con1 and con2
# a=30 b=20 c=50 a>b and a>c => True and False = False
# a=30 b=40 c=10 a>b and a>c => False 
# a=20 b=20 c=20 a>b and a>c => False
# a=10 b=8 c=3   a>b and a>c => True

#Logical or
# con1 and con2
# a=30 b=20 c=50 a>b or a>c => True or False = true
# a=30 b=40 c=10 a>b or a>c => True 
# a=20 b=20 c=20 a>b or a>c => False
# a=10 b=8 c=3   a>b or a>c => True

#Logical not
# a=30 b=40 not(a>b) => true
# a=10 b=3 not(a>b) => False

num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))
num3 = int(input("Enter Third Number"))

if num1==num2==num3:
  print("All the numbers are equal")
else:
  if num1>num2 and num1>num3:
    print("Greatest number is ",num1)
  if num2>num1 and num2>num3:
    print("Greatest number is ",num2)
  if num3>num1 and num3>num2:
    print("Greatest number is ",num3)


 

