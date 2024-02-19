'''
a1=10
a2=100
a3=200

1 ,2  ,5 ,10 

1-Taking Input
2-check divisibility
3-Compare
'''
n1=int(input("Enter First Number"))
n2=int(input("Enter second Number"))
n3=int(input("Enter Third Number"))

#Checking min num
m=min(n1,min(n2,n3))
i=1
cal=0

while i<=m:
  if n1%i==0 and n2%i==0 and n3%i==0:
    cal=i  
  i=i+1

print("GCF of {} , {} and {} is {}".format(n1,n2,n3,cal))




