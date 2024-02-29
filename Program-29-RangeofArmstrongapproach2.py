'''
153
1 = 1*1*1=1
5 = 5*5*5=125
3 = 3*3*3=27

157

1634
1 = 1*1*1*1 =1
6 = 6*6*6*6 =
3 = 3*3*3*3 =
4 = 4*4*4*4 =
1634

1- Calculate the total number of digits
2 - Break the number
3 - Cal power of every digit
4 - add the power
5 - compare with orginal number
6 - Push inside a loop

n>=1 and n<=9 => 1 digit number

256//10 =25
25//10 =2
2//10=0

10//10=1
1//10=0

11/10=1
1//10=0

c=0
5645 //10 =564 -> c=1
564//10 =56 -> c=2
56//10=5 -> c=3
5//10=0 -> c=4



n=496
d=n
c=0

d=d//10 => 496//10 =49 => c=c+1 =1
d=d//10 => 49//10 = 4 => c=c+1 =2
d=d//10 => 4//10 => 0 => c=c+1 =3


d2=n

d2%10 =>6
d2=d2//10 => 49



'''

#Logic to calculate total no of digits in a number
'''
absolute value func
abs()
'''

#Taking input of range from user
n1 =int(input("Enter Start Number"))
n2 =int(input("Enter End Number"))

for n in range(n1,n2+1):
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
#  else:
#    print("{} is not a Armstrong Number".format(n))
  
  


'''
count=3
a=567
cal=0

r=567%10 =7
567//10 =56
cal =cal +(r**count)

r=56%10 =6
56//10 =5
cal =cal +(r**count)

r=5%10 =5
5//10 =0
cal =cal +(r**count)



'''


  

  



