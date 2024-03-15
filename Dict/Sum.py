# a={}
# for x in range(10):
#   num =int(input("Enter a Number"))
#   a[x]= num

# for y in a:
#   print(a[y])

a={1:'apple',2:'orange',3:'banana'}
# for x in a.values():
#   print(x)

# for x in a.keys():
#   print(x)

# for x,y in a.items():
#   print(x," ",y)

a[1]="Potato"

print(a)

a[4]="Potato"

print(a)

a.pop(1)
print(a)

a.popitem()
print(a)

a.clear()
print(a)
