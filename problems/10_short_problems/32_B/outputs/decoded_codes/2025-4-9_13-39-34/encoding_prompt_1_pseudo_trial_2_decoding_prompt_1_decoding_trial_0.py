# 1. Initialize Input
input_string = input().strip()  # Read a line of input and remove unnecessary spaces

# 2. Set Up Variables
index = 0  # Variable to track the position in the input string
result = ""  # Variable to store the output

# 3. Process Each Character
while index < len(input_string):  # While loop to iterate over the characters
    if input_string[index] == '.':  # Check if the current character is a dot
        result += '0'  # Append '0' to result
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check for two consecutive dots
        result += '1'  # Append '1' to result
        index += 2  # Move past both characters
    else:  # Any other case
        result += '2'  # Append '2' to result
        index += 2  # Move past both characters

# 4. Display Output
print(result)  # Print the result
