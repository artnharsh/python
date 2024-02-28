l = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	
	l.append(int(input())) 

print(l)

d = {}

for i in range (0, n):

	if l[i] % 2 == 0 :
		
		d[l[i]] = "even"
	
	elif l[i]% 2 != 0:
		
		d[l[i]] = "odd"
  
print(d)

