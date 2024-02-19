'''
5*4*3*2*1 =120
10*9*8*7*6*5*4*3*2*1 =
'''

n =int(input("Enter a Number"))
i=1
cal=1
while i<=n:
  cal =cal*i
  i=i+1
  
print("Factorial of {} is {}".format(n,cal))
'''
1<=5
cal =1*1 =>1

2<=5
cal =1*2 =>2

3<=5
cal =2*3 =>6

4<=5
cal =6*4 => 24

5<=5
cal =24*5 => 120

'''
