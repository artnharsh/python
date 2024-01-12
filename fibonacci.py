x = int(input("Enter the range of the fibonacci series:\n"))
a = 0
b = 1
c = 0
print(a)
print(b)

for i in range(x):
	c = a + b
	print(c)
	a = b
	b = c
	

