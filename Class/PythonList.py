#Creating class for prime number
class prime:
  
  def checkprime(self,l):
    for x in l:
      count=0
      for y in range(1,x+1):
        if x%y==0:
          count +=1
      
      if count ==2:
        print("{} is a prime number".format(x))
        
        
  
  

a=[2,45,6,78,98,78,12,13]

obj = prime()
obj.checkprime(a)



'''
1- Take a list pass it to function and find out factorial of all the numbers in list 

2- Write a program to reverse the list using class and object without using any built in function

3- Write a program to search a number in a list. If number is available print position of the number else print -1


'''