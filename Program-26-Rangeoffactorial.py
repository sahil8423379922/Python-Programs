#Print the range of factorial where range is given by user
n1=int(input("Enter the First number"))
n2=int(input("Enter the Second Number"))

for x in range(n1,n2+1):
  cal=1
  while x!=0:
    cal =cal*x
    x=x-1
  print(cal)

'''5
n1=1
n2=5



n=10
cal =1*10 =>10

n=9
cal =10*9 =>90

n=8
cal =90*8

'''

