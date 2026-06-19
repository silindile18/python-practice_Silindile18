# Capture information for User 1
name1 = input("Enter first user's name: ")
age1 = int(input("Enter first user's age: "))
height1 = float(input("Enter first user's height in cm: "))

print()

# Capture information for User 2
name2 = input("Enter second user's name: ")
age2 = int(input("Enter second user's age: "))
height2 = float(input("Enter second user's height in cm: "))

print()

# Display user information
print(f"{name1} is {age1} years old and is {height1} cm tall.")
print(f"{name2} is {age2} years old and is {height2} cm tall.")

print()

# Calculate and display total combined height
total_height = height1 + height2

print(f"The total combined height of both users is {total_height} cm.")