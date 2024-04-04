class code:
 def reverse(self,l):
   revlist=[]
   '''
   len(l)-1 => giving last position of the list
   -1 => indicating that loop will run till zero
   -1 => moving the loop in the reverse order
   '''
   for x in range(len(l)-1,-1,-1):
     revlist.append(l[x])
     
   return revlist

obj =code()
l =[]
for x in range(10):
  n =int(input("Enter a Number"))
  l.append(n)

print("Orginal List is {}".format(l))
  
ans =obj.reverse(l)

print("Reversed List is {}".format(ans))
  
