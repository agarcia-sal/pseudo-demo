# Read Input
user_input = input()

# Initialize Variables
index = 0
result = ""

# Process Each Symbol
while index < len(user_input):
    if user_input[index] == ".":
        result += "0"
        index += 1
    else:
        if index + 1 < len(user_input) and user_input[index + 1] == ".":
            result += "1"
            index += 2
        else:
            result += "2"
            index += 2

# Output the Result
print(result)
