#Print the range of composite number where range is given by the user
n1=int(input("Enter the First Number"))
n2=int(input("Enter the Second Number"))

for a in range(n1,n2+1):
 count=0
 for x in range(1,a):
   if a%x ==0:
     count =count+1

 if count>=2:
   print("{} is a Composite Number and it it's count is {}".format(a,count))
 else:
   print("{}  is not a Composite Number".format(a))