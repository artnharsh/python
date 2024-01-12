sum = 0
n = int(input("Enter the range:\n"))
for i in range(1,n+1,1) :
	sum = sum + i
print("Sum of first {} natural numbers is: {}\n".format(n,sum))

