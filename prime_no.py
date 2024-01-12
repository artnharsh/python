x=int(input("Enter your number here:\n"))
i=2;
while i<x :
	if x == 0 or x == 1 :
		print("Number is neither prime nor composite")
	elif x%i == 0:
		print("Number is not prime")
		break
	else:
		print("Number is prime")
		break
	i+=1

