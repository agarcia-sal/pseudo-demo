# Step 1: Receive Input
input_string = input().strip()  # Read input and remove leading/trailing whitespace

# Step 2: Initialize Variables
current_index = 0  # Initialize index for traversing the input string
output_string = ''  # Initialize an empty string to store the output

# Step 3: Process the Input String
while current_index < len(input_string):
    if input_string[current_index] == '.':
        # If the current character is a dot
        output_string += '0'  # Append '0' to output string
        current_index += 1  # Move to the next character
    elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
        # If the next character is also a dot
        output_string += '1'  # Append '1' to output string
        current_index += 2  # Skip the next character
    else:
        # If no dot or next character is not a dot
        output_string += '2'  # Append '2' to output string
        current_index += 2  # Skip the next character

# Step 4: Output the Result
print(output_string)  # Display the final numeric representation
