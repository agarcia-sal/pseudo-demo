# Step 1: Import Required Libraries
import sys  # Imported to provide access to system-specific parameters and functions

# Step 2: Read Input
input_string = input().strip()  # Read a string input and remove any extra spaces

# Step 3: Initialize Variables
index = 0  # Set variable to track the current position within the string
result = ""  # Create an empty string to store the translated output

# Step 4: Process the Input String
while index < len(input_string):  # While index is less than the length of input string
    if input_string[index] == '.':  # If the current character is a dot
        result += '0'  # Append '0' to the result
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check if next character is also a dot
        result += '1'  # Append '1' to the result
        index += 2  # Skip both characters
    else:  # Otherwise (handle any other character)
        result += '2'  # Append '2' to the result
        index += 2  # Skip both characters

# Step 5: Output the Result
print(result)  # Print the translated numeric representation
