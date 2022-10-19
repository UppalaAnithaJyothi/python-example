"""
FizzBuzz is a classic programming challenge.

For every number from 1 to n,
print Fizz if the number is divisible by 3,
print Buzz if the number is divisible by 5,
print FizzBuzz if the number is divisible by 3 and 5,
otherwise, print the original number otherwise
"""

 
# Todo: Write a function that returns:
#  "Fizz" if the number is divisible by 3
#  "Buzz" if the number is divisible by 5
#  "FizzBuzz" if the number is divisible by 3 and 5
#  the number otherwise

def Fizz_Buzz(n):
    l=[]
    for i in range(1,n+1):
        if i%15==0:
            l.append("FizzBuzz")
        elif i%3==0:
            l.append("Fizz")
        elif i%5==0:
            l.append("Buzz")
        else:
            l.append(i)
    return l
# Todo: Test the function
# print(Fizz_Buzz(15))

# Todo: Request a number from the user
# n = int(input("Enter a number"))
# print(Fizz_Buzz(n))
# Todo: Print a list of fizz-buzzed numbers from 1 to the given number
n = int(input("Enter the range"))
print(Fizz_Buzz(n))

