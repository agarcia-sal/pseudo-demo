# Step 1: Read a line of input that contains a string of characters
input_string = input()

# Step 2: Initialize variables
current_index = 0  # To track our position in the input string
output_string = ""  # To store the results

# Step 3: Processing loop
while current_index < len(input_string):  # Continue until we reach the end of the string
    # Check the character at the current index
    if input_string[current_index] == ".":  # If the character is a dot
        output_string += '0'  # Append '0' to the output string
        current_index += 1  # Move to the next character
    elif current_index + 1 < len(input_string) and input_string[current_index + 1] == ".":  
        # If the next character is also a dot
        output_string += '1'  # Append '1' to the output string
        current_index += 2  # Skip the next character
    else:  # If the next character is not a dot
        output_string += '2'  # Append '2' to the output string
        current_index += 2  # Also skip the next character

# Step 4: Output the resulting output string
print(output_string)
