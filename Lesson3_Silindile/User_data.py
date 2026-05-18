# Function to calculate total height
def calculate_total_height(users):
    total = 0

    for user in users:
        total += user["height"]

    return total


# List to store user dictionaries
users = []

# Capture information for 2 users
for i in range(2):
    print(f"\nEnter details for User {i + 1}")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height in cm: "))

    # Dictionary for each user
    user = {
        "name": name,
        "age": age,
        "height": height
    }

    # Add dictionary to list
    users.append(user)

# Display user information
print("\nUser Information:")

for user in users:
    print(f"{user['name']} is {user['age']} years old and has a height of {user['height']} cm.")

# Calculate and display total combined height
total_height = calculate_total_height(users)

print(f"\nThe total combined height of both users is {total_height} cm.")