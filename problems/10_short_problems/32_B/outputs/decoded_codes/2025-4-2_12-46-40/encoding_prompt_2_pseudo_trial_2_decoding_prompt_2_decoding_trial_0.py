# Step 1: Input - Read a line of input that contains a string of characters
input_string = input()

# Step 2: Initialize Variables
current_index = 0
output_string = ""

# Step 3: Processing Loop
while current_index < len(input_string):
    # Check the character at the current index
    if input_string[current_index] == '.':
        # Append '0' to the output string
        output_string += '0'
        # Move to the next character
        current_index += 1
    elif (current_index + 1 < len(input_string) and 
          input_string[current_index + 1] == '.'):
        # Append '1' to the output string
        output_string += '1'
        # Skip the next character
        current_index += 2
    else:
        # Append '2' to the output string
        output_string += '2'
        # Also skip the next character
        current_index += 2

# Step 4: Output - Display the resulting output string
print(output_string)
