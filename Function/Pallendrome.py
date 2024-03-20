#Function to calculate number is pallendrome or not
def pallendrome(num):
  cal=0
  
  #Logic to reverse the number
  while num!=0:
    r=num%10
    cal=(cal*10) + r 
    num=num//10
  #Passing data back to main body
  return cal
 
#Taking input from user 
n =int(input("Enter a Number"))

#Passing value inside the function  
ans=pallendrome(n)

if n==ans:
  print(" {} is a Pallendrome Number".format(n))
else:
  print(" {} is not a Pallendrome Number".format(n))

    
    
  


