# Step 1: Read Input
input_string = input().strip()  # Obtain input string and remove extra spaces

# Step 2: Initialize Variables
index = 0  # Counter to track current position in the string
output_string = ""  # Accumulator for the result

# Step 3: Process Input Until End
while index < len(input_string):  # Continue until the end of the string
    if input_string[index] == '.':  # Check if the current character is a dot
        output_string += '0'  # Append '0' to the output string
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check next character for dot
        output_string += '1'  # Append '1' to the output string
        index += 2  # Skip to the character after next
    else:  # No dots found in the conditions above
        output_string += '2'  # Append '2' to the output string
        index += 2  # Skip to the character after next

# Step 4: Output Result
print(output_string)  # Print the final output string
