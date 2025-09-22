# Start Program

# Read input from standard input
input_string = input().strip()  # Remove any extra whitespace
index = 0
result = ""

# Loop through the input string until the end is reached
while index < len(input_string):

    # Check if the current character is a dot
    if input_string[index] == '.':
        result += '0'  # Append '0' to the result string
        index += 1  # Move to the next character
    
    # Check if the next character is a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Append '1' to the result string
        index += 2  # Move forward two characters
    
    # If the next character is not a dot
    else:
        result += '2'  # Append '2' to the result string
        index += 2  # Move forward two characters

# Output the final result string
print(result)

# End Program
