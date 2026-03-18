1.
# What is a Function?
2.
#A function is a block of code that runs only when it is called.

# Why use Functions
# 1. Avoid repeating code
 # 2. Makes program clean & organized
 # 3. Easy to debug and reuse
# Syntax:
# def function name():
# code


 #def greet:

#function with parameters
#used to pass values
 


#1. create a function to calculate and return result 
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

#2. create a function to check if a whether is even or odd
def check_even_odd(num):
   if num % 2 ==0:
      return "Even"
   else:
         return "Odd"

#3. create a function to find the factorial of a number
def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


#4.find a maximum number
def find_max (a, b, C):
   if a >= b and a >= c:
      return a
   elif b >= a and b >= c:
      return b 
   else:
      return c
a = float(input("Enter first number: "))
b = float(input ("Enter second number: "))
c = float(input("Enter third number: "))
result = find_max(a, b, c)
print (f"The greatest number is: (result)")


#5. create a function to check if a string is palindronr

def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    import string
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    
    return s == s[::-1]
    print(is_palindrome("Madam"))           # True
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("Hello"))           # False

#6.create a function to calculate the area of circle
def area_of_circle(radius):
   return 3.14 * radius ** 2

radius = float(input("enter radius of the circle:" ))
area = area_of_circle(radius)
print("the area of the circle is:(radius)")