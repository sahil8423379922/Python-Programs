#Operators
'''
Operator is something which we use to perform any type of operation-
1- Arithmatic Operators
 -Addition + => 6+5
 -Subtraction - => 6-5
 -Multiplication => 9*10
 -Division
  -Floor Division // = > 5//2 =2
  -Modulus % =>  90%10 =0
  -Simple Division / => 5/2 =2.5

  
  90/10=9 and remainder =0
  5/2 =2 and remainder =1
  5/2 =2.5 and remainder=0

  2-Assignment Operator
    - simple assignment operator  => a=4

    - Addition and Assignment Operator => 
      a=6 => a+=4 => a=a+4 => 10
      a=-10 => a+=3 => a=a+3 => a= -10 +3 => -7

    - Subtraction and Assignment Operator
      a=5 => a-=3 => a=a-3 => a=5-3 => 2
    
    - Multiplication and Assignment Operator
      a=4 => a*=5 => a=4*5 => 20

    - Floor Division and Assignment Operator
      a=5 => a//=5 => 1
    
    - Division and Assignment Operator
      a=5 => a/=2 => 2.5

    - Modulus and Assignment Operator
      a=10 => a%=10 => a=a%10 =>0
    
'''

#Arithmatic Operators

a= int(input("Enter First Number"))
b= int(input("Enter Second Number"))

cal =a+b

print("Addition of ",a," and ",b," is ",cal)

print("Addition of {} and {} is {}".format(a,b,a+b))
print("Subtraction of {} and {} is {}".format(a,b,a-b))
print("Multiplication of {} and {} is {}".format(a,b,a*b))
print("Floor Divison of {} and {} is {}".format(a,b,a//b))
print("Remainder of {} and {} is {}".format(a,b,a%b))
print("Division of {} and {} is {}".format(a,b,a/b))


