def input():
    n=int(input("Enter the numbers of the element:\n"))
    numbers=[]
    for i in range(0,n+1,1):
        numbers.append(input())
    return numbers

def max_number(numbers):
    return max(numbers)

def min_number(numbers):
    return min(numbers)

def calc_min(numbers):
    return sum(numbers)/len(numbers)


numbers = input()
print("The maximum number is:",max_number(numbers))
print("The minimum number is:",min_number(numbers))
print("The average of all numbers is:",calc_min(numbers))
