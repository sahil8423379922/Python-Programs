#Printing the range of prime numbers
# n1 =int(input("Enter the First Number"))
# n2 =int(input("Enter the Second Number"))

# for x in range(n1,n2+1):
#   print(x)
  
a=4
for y in range(1,a):
  if a%y==0:
    print("{} is not a prime number".format(a))
    break
if a-1 ==y:
  print("{} is a prime number".format(a))
  
  
'''
a=13
y = > 1 to 12
y=1
13%1==0 

y=2
13%2==0

y=3
13%3==0

y=4
13%4==0

y=5
13%5==0

y=6
13%6==0

y=7
13%7==0

y=8
13%8==0

y=9
13%9==0

y=10
13%10==0

y=11
13%11==0

y=12
13%12==0

y=12


if 13-1 ==12:-> it is a prime number


a=4
y -> 2 to 3

y=2
if 4%2==0 => It is not a prime number -> break

y=3

if 4-1 ==2
'''  
  


  