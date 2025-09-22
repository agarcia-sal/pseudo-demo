# Start Program

# Accept Input: Read a line of input from the user and clean it
inputString = input().strip()

# Initialize Variables: Track current position and build output
index = 0
result = ""

# Process Input: Loop through inputString based on the defined rules
while index < len(inputString):
    if inputString[index] == ".":
        # If current character is a dot
        result += "0"
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == ".":
        # If the next character is also a dot
        result += "1"
        index += 2  # Move ahead by two positions
    else:
        # If the character is not a dot
        result += "2"
        index += 2  # Move ahead by two positions

# Output the Result: Display the final numeric string
print(result)
