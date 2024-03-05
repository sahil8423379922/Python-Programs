#Find the Max and Min in List
a=[]
for x in range(10):
  n=int(input("Enter a number :"))
  a.append(n)
  
max =max(a)
min=min(a)
print("Maximum of the list is {}".format(max))
print("Minimum of the list is  {}".format(min))
  