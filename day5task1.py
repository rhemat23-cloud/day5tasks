
def create_user(name, age, role):
    """
    Create a user dictionary with formatted name.
    :param name: str - User's name
    :param age: int - User's age
    :param role: str - User's role
    :return: dict - User information
    """
    # Input validation
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer.")
    if not isinstance(role, str) or not role.strip():
        raise ValueError("Role must be a non-empty string.")

    # Return user dictionary with formatted name
    return {
        "name": name.title(),  # Capitalize each word
        "age": age,
        "role": role
    }

# List to store multiple users
users = []

# Adding users
try:
    users.append(create_user("ranju", 28, "developer"))
    users.append(create_user("raju", 32, "designer"))
    users.append(create_user("hhemug", 25, "tester"))
except ValueError as e:
    print(f"Error: {e}")

# Printing all users
print("\nAll Users:")
for idx, user in enumerate(users, start=1):
    print(f"{idx}. Name: {user['name']}, Age: {user['age']}, Role: {user['role']}")

