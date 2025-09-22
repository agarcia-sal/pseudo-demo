# Step 1: Read input string and strip whitespace
input_string = input().strip()

# Step 2: Initialize index for tracking position in the string
current_index = 0 

# Step 3: Initialize output string to store the result
output_string = ""

# Step 4: While the index is less than the length of the string
while current_index < len(input_string):
    # Check if the current character is a dot (.)
    if input_string[current_index] == '.':
        output_string += '0'  # Append '0' for a single dot
        current_index += 1  # Move to the next character
    # Check if the next character is also a dot (..)
    elif (current_index + 1 < len(input_string) and input_string[current_index + 1] == '.'):
        output_string += '1'  # Append '1' for two dots
        current_index += 2  # Skip the next character
    else:
        output_string += '2'  # Append '2' for a non-dot character
        current_index += 2  # Move to the character after next

# Step 5: Print the final output string containing the converted representation
print(output_string)
