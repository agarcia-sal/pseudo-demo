# Start of the program to decode a specific sequence of characters
# from an input string into a new numerical representation.

# Step 1: Accept a string of characters from the user
input_string = input()

# Step 2: Initialize variables
i = 0  # Index counter
decoded_output = ""  # This will store the result of the decoding process

# Step 3: Process the input string
while i < len(input_string):  # Loop until we reach the end of the input string
    # Check if the current character is a dot
    if input_string[i] == '.':
        decoded_output += '0'  # Append '0' to the output
        i += 1  # Move to the next character
    # Check if the next character is also a dot
    elif i + 1 < len(input_string) and input_string[i + 1] == '.':
        decoded_output += '1'  # Append '1' to the output
        i += 2  # Skip to the character after next
    # If current character is a hyphen
    else:
        decoded_output += '2'  # Append '2' to the output
        i += 2  # Skip to the character after next

# Step 4: Output the result
print(decoded_output)  # Print the final decoded output
