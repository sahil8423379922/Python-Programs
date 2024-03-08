a=[1,454,34,657,244]

'''
y="Computer"
y[0]= "c" =-8
y[1]="o" =-7
y[2]="m" =-6
y[3]="p" =-5
y[4]="u" =-4
y[5]="t" =-3
y[6]="e" =-2
y[7]="r" =-1

y[0:4:1] = comp
y[:4:1]=comp
y[::-1] ="retupmoc"

'''


for x in a:
 if str(x)==str(x)[::-1]:
   print("{} is a Pallendrome Number".format(x))
 else:
   print("{} is Not a Pallendrome Number".format(x))
   
