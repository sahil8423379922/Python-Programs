a=[]
for x in range(10):
  n=int(input("Enter a number :"))
  a.append(n)
  
for x in a:
  if x%2==0:
    print("Even Number =",x)