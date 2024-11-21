
# Basic Function Definition and Calling
# def greet():
#     print("Hello, welcome to the Python function tutorial!")

# greet()  # Call to the function

# # Function with Parameters and Arguments
# def greet_person(name):
#     print(f"Hello, {name}!")

# greet_person("Dionysios")  # Passing an argument

# # Function with Return Statement
def add(a, b):
    return a + b

# result = add(10, 5)  # Call and store the result
# print(f"The result is: {result}")


# # Built-in Functions: print(), input(), type()
# name = input("Enter your name: ")  # User input
# print(f"Hello, {name}")  # Using print
# print(type(name))  # Using type


# # User-Defined Function (UDF) Example
def multiply(x, y):
    return x * y

# print(multiply(4, 5))  # Calling the UDF


# # Anonymous Function (Lambda)
# square = lambda x: x * x  # Lambda function
# result = square(6)
# print(result)  # Output: 36

# multiply_lambda = lambda x, y: x * y
# print(multiply_lambda(3, 4))  # Output: 12

# hello = lambda input: print(f"Hello, {input}!")

# # Function of Functions (Calling functions within functions)
# def multiply_and_add(x, y, z):
#     result = multiply(x, y)  # Calls the multiply function
#     return add(result, z)     # Adds z to the product

#print(multiply_and_add(2, 3, 5))  # Output: 11


# # Global vs Local Variables Example
# name = "Global Name"  # Global variable

# def greet_local():
#     name = "Local Name"  # Local variable
#     print(f"Inside function: {name}")

# greet_local()  # Output: Inside function: Local Name
# print(f"Outside function: {name}")  # Output: Outside function: Global Name


# # Arbitrary Arguments (*args)

# def my_function(*args):
#     for arg in args:
#         print(arg)

# my_function(1, 2, 3, "Hello")  # Arbitrary number of arguments


# # Keyword Arguments (**kwargs)
# def greet_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# greet_kwargs(name="Dionysios", age=30, city="Athens")
# # Output:
# # name = Dionysios
# # age = 30
# # city = Athens


# # Default Parameter Values
# def greet_default(name="Stranger"):
#     print(f"Hello, {name}!")

# greet_default()  # Output: Hello, Stranger!
# greet_default("Dionysios")  # Output: Hello, Dionysios!


# # Recursive Function (Factorial)
# def factorial(n):
#     if(n==0):
#         return 1
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # print(factorial(65))  # Output: 120

# sixtyFiveFactorial = factorial(65)
# # Passing Functions as Arguments
# def apply_function(func, value):
#     return func(value)

# def square(x):
#     return x * x

# print(apply_function(square, 4))  # Output: 16


# # Using map() with Lambda
# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)  # Output: [1, 4, 9, 16]

# # Function that prints a generic greeting message
# def greet():
#     print("Hello from inside the loop!")

# # Calling the function inside the loop, but not using the loop's variable
# for i in range(5):
#     greet()  # The loop iterates 5 times, but 'i' is not used inside the function
# # Function that squares a number
# def square(number):
#     return number ** 2

# # # Using the loop's iterating variable inside the function
# for i in range(1, 6):
#     print(f"The square of {i} is: {square(i)}")

# # Function that converts a string to uppercase
def to_uppercase(input):
    if isinstance(input,str):
        return input.upper()
    else:
        return input   

# Specified array (list of strings)
names = ["dionysios", "python", "functions", "loop",1]

# Looping over the array and using the function
for name in names:
    print(f"{name} in uppercase is: {to_uppercase(name)}")
