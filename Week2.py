# Conditions

# If statement
# x = 7
# if x > 5:
#     print("x is greater than 5")  # Output: x is greater than 5

# If-else statement
# y = 5
# if y % 2 == 0:
#     print("y is even")
# else:
#     print("y is odd")  # Output: y is odd

# # Nested if statement
# z = 7
# if z > 5:
#     print("z is greater than 5")  # Output: z is greater than 5
#     if z % 2 == 0:
#         print("z is also even")   # Output: z is also even
#     else:
#         print("z is odd")
# else:
#     print("z is 5 or less")

# # If-elif-else statement
# score = 85

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'  # This block executes
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
# print(f"Your grade is {grade}")   # Output: Your grade is B

# # Loops
# # For loop – Iteration for a number of specified times
# print("For loop with specified iterations:")
# for i in range(1,6): #[1,2,3,4,5]
#     print("Iteration {i}")  # Iterates from 1 to 5

# # Range - integers
# print("Using range to generate numbers:")
# for num in range(2, 7): #[2,3,4,5,6] + [1,1,1,1,1] = [3,4,5,6,7]
#     print(num+1)  # Outputs numbers from 3 to 7

# Count starts from 0
# print("Counting starting from 0:")
# for count in range(3): #[0,1,2]
#     print(count)  # Outputs 0, 1, 2

# # For loop in lists
# fruits = ['apple', 'banana', 'cherry']
# print("Iterating over a list:")
# for fruit in fruits:
#     print(f"I like {fruit}")  # Outputs each fruit in the list
# print("Done")
# # While loop - Executes as long as a condition is True
# print("While loop example:")
# n = 0
# while n < 3:
#     n += 1
#     print(f"n is {n}")  # Outputs n values from 0 to 2

# # Break – Exits loop prematurely
# print("Using break in a loop:")
# for number in range(5): #[0,1,2,3,4]
#     if number == 3:
#         print("Breaking the loop")
#         break  # Exits the loop when number is 3
#     print(number)

# # Continue - Skips the current iteration and starts the next one
# print("Using continue in a loop:")
# for number in range(5):
#     if number == 2:
#         print("Skipping number 2")
#         continue  # Skips the rest of the loop when number is 2
#     print(number)
# # Asking for a number and checking if it's even or odd

# number = int(input("Enter a number: "))  # User inputs a number

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")
# # Asking for a number and checking if it's even or odd
# number = int(input("Enter a number: "))  # User inputs a number

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")
# # Asking for a number and checking if it's even or odd
# number = intf(input("Enter a number: "))  # User inputs a number

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")
# # Asking for a score and assigning a grade
# score = int(input("Enter your score (0-100): "))
# if score>100 or score < 0:
#     print("wrong score!!")
# else:
#     if score >= 90:
#         print("You got an A!")
#     elif score >= 80:
#         print("You got a B!")
#     elif score >= 70:
#         print("You got a C.")
#     elif score >= 60:
#         print("You got a D.")
#     else:
#         print("You got an F.")

# # Continue the loop if the user enters an empty string

for i in range(5): 
    for j in range(10):
        name = input("Enter a name (leave empty to skip): ")
        if name == '':
            print("Skipped!")
            continue  # Skips the rest of the loop and starts the next iteration
        print(f"Hello, {name}!, number: {i}")
