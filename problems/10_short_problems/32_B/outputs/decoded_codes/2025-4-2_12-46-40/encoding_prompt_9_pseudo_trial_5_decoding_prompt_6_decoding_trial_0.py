# Step 1: Receive Input
input_string = input().strip()  # Read input string and remove surrounding whitespace

# Step 2: Initialize Variables
index = 0  # Track the current position in the input string
output_string = ""  # To store the resulting numeric representation

# Step 3: Process the Input String
while index < len(input_string):
    if input_string[index] == '.':
        output_string += '0'  # Append '0' for a single dot
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        output_string += '1'  # Append '1' for a pair of dots
        index += 2  # Skip to the character after the next
    else:
        output_string += '2'  # Append '2' for other characters
        index += 2  # Skip to the character after the next

# Step 4: Output the Result
print(output_string)  # Print the converted numerical representation
