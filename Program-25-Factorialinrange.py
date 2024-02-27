n1=int(input("Enter First Number"))
n2=int(input("Enter Second Number"))

for a in range(n1,n2+1):
  cal=1
  while a!=0:
    cal=cal*a
    a=a-1
  print(cal)