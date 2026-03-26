# Python code for file handling: 
user_details = [
    {"name": "raj", "age": 25, "role": "Developer"},
    {"name": "mugil", "age": 30, "role": "Designer"},
    {"name": "magil", "age": 28, "role": "Team Lead"}
]

# 1. Create and write to the file
with open("team_data.txt", "w") as file:  # 'w' mode will create or overwrite the file
    for user in user_details:
        line =(f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']})
"
        file.write(line)

# 2. Read and display the content of the file
with open("team_data.txt", "r") as file:  # 'r' mode for reading
    content = file.read()

print("Contents of team_data.txt:
")
print(content)

# Optional: read line by line
print("Reading line by line:
")
with open("team_data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes extra newline characters
