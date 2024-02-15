amt = int(input("Enter the Amount"))

#Creating variables to store notes
n500 = n200 =n100 = n50 =n20 = n10 =n5 =n2 =n1 =0

#Condition

if amt >=500:
  #Cal total notes of 500
  n500= amt//500
  #Cal remaining amount
  amt = amt%500
  #amt%=500
  
if amt >=200:
  #Cal total notes of 500
  n200= amt//200
  #Cal remaining amount
  amt = amt%200
  
if amt >=100:
  #Cal total notes of 500
  n100= amt//100
  #Cal remaining amount
  amt = amt%100
  
if amt >=50:
  #Cal total notes of 500
  n50= amt//50
  #Cal remaining amount
  amt = amt%50
  
if amt >=20:
  #Cal total notes of 500
  n20= amt//20
  #Cal remaining amount
  amt = amt%20
  
if amt >=10:
  #Cal total notes of 500
  n10= amt//10
  #Cal remaining amount
  amt = amt%10
  
if amt >=5:
  #Cal total notes of 500
  n5= amt//5
  #Cal remaining amount
  amt = amt%5
  
if amt >=2:
  #Cal total notes of 500
  n2= amt//2
  #Cal remaining amount
  amt = amt%2
  
if amt >=1:
  #Cal total notes of 500
  n1= amt//1
  #Cal remaining amount
  amt = amt%1
  
  
#Printing Result
print("Total No. of 500 notes = ",n500)
print("Total No. of 200 notes = ",n200)
print("Total No. of 100 notes = ",n100)
print("Total No. of 50 notes = ",n50)
print("Total No. of 20 notes = ",n20)
print("Total No. of 10 notes = ",n10)
print("Total No. of 5 notes = ",n5)
print("Total No. of 2 notes = ",n2)
print("Total No. of 1 notes = ",n1)


 
  
  
