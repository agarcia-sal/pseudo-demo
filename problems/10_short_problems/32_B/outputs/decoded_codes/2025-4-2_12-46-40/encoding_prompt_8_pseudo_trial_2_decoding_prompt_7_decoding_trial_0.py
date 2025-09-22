# Start of the program to translate a sequence of symbols into a numeric representation

# Read Input
input_string = input().strip()  # Get a string of symbols and remove extra spaces

# Initialize Variables
index = 0  # To track the current position in the string
result = ''  # To store the translated numbers

# Process the String
while index < len(input_string):  # While we have not reached the end of the string
    if input_string[index] == '.':
        result += '0'  # If current character is a dot, append '0' to result
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # If next character is also a dot, append '1' to result
        index += 2  # Move past the two symbols
    else:
        result += '2'  # If no dots are encountered in the previous conditions, append '2'
        index += 2  # Move past the two symbols

# Output Result
print(result)  # Display the translated string result

# End of the program
