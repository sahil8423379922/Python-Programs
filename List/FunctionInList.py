#Length Function
a=[1,2,3,4,5,6]

l = len(a)

print("Length of List is ",l)

#Append Function
a.append(0)

print(a)

#Extend Function
b=[10,23,43,54]
a.extend(b)

print("After Extending list =",a)

#Insert Function
a.insert(6,7)
print("List after inserting element =",a)

#Remove Function
a.remove(7)
print("After Removing the element =",a)

#Removing the last element in list
a.pop()
print("After pop =",a)

#Removing all the elements from the list
#a.clear()
#print("After Clear",a)

#Get the position of any element
i =a.index(10)
print("Position of the 10 is =",i)

#Calculate the occurance
a.append(10)
print(a)
c =a.count(10)
print("Count of 10 =",c)

#Soting the list

#Ascending order sorting 
a.sort()
print("After Ascending Sortng =",a)

a.sort(reverse=True)
print("After Descending sort =",a)

#Reverse Function
a.reverse()
print("After Reversing the list =",a)

#Create copy of your list
n =a.copy()
print(n)

#Sorted Method
cn=sorted(a,reverse=True)
print(a)
print(cn)

#Max function
g=max(a)
print("greatest number =",g)

#Min Function
m=min(a)
print("Smallest Number =",m)

#Sum Function
su =sum(a)
print("Sum of all elements =",su)

#any function
b =[True,False,False,True]
print(any(b))

a=10
b=20
c=30
d=0
c=[a+b>10,a+c!=40,a+d==30]
print(any(c))

#all
print(all(c))

#zip function
a=[1,2,3]
b=['apple','banana','potato']
#[[1,'apple'],[2,'banana'],[3,'potato']]
for x in zip(a,b):
  print(x,end=" ")













