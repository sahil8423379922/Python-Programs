'''
1-First loop is to get number to find factor
2-Finding the factor for given number
'''

n1=int(input("Enter a Number"))
n2=int(input("Enter a Number"))

for x in range(n1,n2+1):
  for y in range(1,x+1):
    if x % y ==0:
      print("{} is the factor of {}".format(y,x))
  print()
  
  '''
  n1=1
  n2=4
  
  x-> 1to4
  x=1
  
  y -> 1 to 1
  y=1
  1%1 == 0 => 1 is the factor of 1
  
  x=2
  y -> 1 to 2
  y=1
  2%1 ==0 => 1 is fac of 2
  y=2
  2%2 ==0 => 2 is fac of 2
  
  x=3
  y -> 1 to 3
  3%1 == 0 => 1 is fac of 3
  y=2
  3%2 ==0
  y=3
  3%3 ==0 =>3 is fac of 3
  
  x=4
  y -> 1 to 4
  y=1
  4%1 ==0 => 1 is fac of 4
  y=2
  4%2 ==0 => 2 is fac of 4
  y=3
  4%3==0
  y=4
  4%4==0 => 4 is fac of 4
  
  
  
  
  '''