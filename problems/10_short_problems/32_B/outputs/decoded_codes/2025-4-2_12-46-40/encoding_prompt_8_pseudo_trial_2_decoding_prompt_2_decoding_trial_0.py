# Start

# Read Input
input_string = input().strip()  # Get a string of symbols and remove extra spaces

# Initialize Variables
index = 0  # Set a counter to track the current position in the string
result = ""  # Create an empty string to store the translated numbers

# Process the String
while index < len(input_string):  # While the counter index is less than the length of the string
    if input_string[index] == '.':  # If the current character is a dot
        result += '0'  # Append '0' to result
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check if the next character is also a dot
        result += '1'  # Append '1' to result
        index += 2  # Move past the two symbols
    else:  # Else case if there is no dot at the current index
        result += '2'  # Append '2' to result
        index += 2  # Move past the two symbols

# Output Result
print(result)  # Display the translated string result

# End
