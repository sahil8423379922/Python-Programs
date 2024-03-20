def check(num):
  if num%2==0:
    return True
  else:
    return False
  
n =int(input("Enter a number :"))
ans = check(n)

if ans:
  print("{} is a even number".format(n))
else:
  print("{} is a odd number".format(n))
  
  