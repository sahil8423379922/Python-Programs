even=[]
a=[]
for x in range(10):
  n=int(input("Enter a number :"))
  a.append(n)
  
for x in a:
  if x%2==0:
    even.append(x)
    
print("Max Even Number is =",max(even))