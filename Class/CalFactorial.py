class code:
 def factorial(self,l):
   for n in l:
     cal=1
     for m in range(1,n+1):
       cal =cal *m
     
     print("Factorial of {} is {}".format(n,cal))

obj =code()     
a=[]
for x in range(10):
  v= int(input("Enter a Number"))
  a.append(v)
  
obj.factorial(a)