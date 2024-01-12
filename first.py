x=int(input("Enter your first number here:\n"))
y=int(input("Enter your second number here:\n"))
c=x&y
print("Use of the and operator:\n",c) 
d=x|y
print("Use of the or operator:\n",d)
print("Use of the negation:\n",~x,~y)
print("Use of the XOR operator:\n",x^y)
print("Value of the x and y was {} and {} respectively\n".format(x,y))
if x>0 and y>0:
	print("Both numbers are positive")
elif x<0 and y<0 :
	print("Both numbers are negative")
elif x<0 and y>0:
	print("x is negative and y is positive")
elif x>0 and y<0 :
	print("x is positive and y is negative")
else :
	print("Both are equal to 0")

