a=[121,153,2323432,123]

for n in a:
#Converting negative into positive and making a copy
 cal=0
 d2=abs(n)
 
#Logic to cal power of Individual digit
 while d2!=0:
   r=d2%10
   d2=d2//10
   cal =cal+(r**len(str(n)))

#Checking number is armstrong or not
 if cal==abs(n):
   print("{} is a Armstrong Number".format(n))