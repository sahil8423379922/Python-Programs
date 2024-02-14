#Display Menu to user
print("Please select the operation :- ")
print("Press 1 for Addition")
print("Press 2 for Sbtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

#Taking input from the user
c = int(input("Select the Operation : "))

# num1 =int(input("Enter the First Number "))
# num2 =int(input("Enter the Second Number"))


# if c==1:
#   cal =num1 +num2
#   print("Addition of {} and {} is {}".format(num1,num2,cal))
# elif c==2:
#   cal = num1-num2
#   print("Subtraction of {} and {} is {}".format(num1, num2 , cal))
# elif c==3:
#   cal = num1 *num2
#   print("Multiplication of {} and {} is {}".format(num1,num2,cal))
# elif c==4:
#   q =num1/num2
#   r =num1%num2
#   print("Division of {} and {} gives {} as Quotient and  {} as Remainder".format(num1,num2,q,r))
# else:
#   print("Enter Valid Operation")


if c<1 or c>4:
  print("Please Enter the Valid Operation")
else:
  num1 =int(input("Enter the First Number "))
  num2 =int(input("Enter the Second Number"))

  if c==1:
    cal =num1 +num2
    print("Addition of {} and {} is {}".format(num1,num2,cal))

    # print("Addition of {} and {} is {}".format(num1,num2,num1+num2))

    # print("Addition of ",num1," and ",num2," is ",num1+num2)
  elif c==2:
    cal = num1-num2
    print("Subtraction of {} and {} is {}".format(num1, num2 , cal))
  elif c==3:
    cal = num1 *num2
    print("Multiplication of {} and {} is {}".format(num1,num2,cal))
  elif c==4:
    q =num1/num2
    r =num1%num2
    print("Division of {} and {} gives {} as Quotient and  {} as Remainder".format(num1,num2,q,r))





