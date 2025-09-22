# Step 1: Read a line of input from the user and remove any extra spaces
input_string = input().strip()  # Storing the cleaned input in input_string

# Step 2: Initialize the variable to keep track of the current position in the input string
index = 0
# Create an empty string to store the final result
output_string = ""

# Step 3: Process the input string character by character
while index < len(input_string):  # Continue until we reach the end of input_string
    if input_string[index] == '.':
        # If the current character is '.', add '0' to output_string
        output_string += '0'
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # Check if the next character is also '.', add '1' to output_string
        output_string += '1'
        index += 2  # Move past both characters
    else:
        # If neither condition is met, add '2' to output_string
        output_string += '2'
        index += 2  # Move past both characters

# Step 4: Print the final numerical representation of the input string
print(output_string)
