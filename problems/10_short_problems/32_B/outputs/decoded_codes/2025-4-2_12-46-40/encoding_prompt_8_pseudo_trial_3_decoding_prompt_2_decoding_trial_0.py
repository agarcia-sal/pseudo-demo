# Step 1: Define Input Source
input_string = input().strip()  # Read the input and remove any extra spaces

# Step 2: Initialize Variables
current_position = 0  # Position in the input string
result = ""  # Final output string

# Step 3: Process the Input String
while current_position < len(input_string):
    if input_string[current_position] == '.':
        result += '0'  # Add '0' if current character is a dot
        current_position += 1  # Move to the next character
    elif current_position + 1 < len(input_string) and input_string[current_position + 1] == '.':
        result += '1'  # Add '1' for a pair of dots
        current_position += 2  # Move ahead by 2 positions
    else:
        result += '2'  # Add '2' for any other character configuration
        current_position += 2  # Move ahead by 2 positions

# Step 4: Output the Result
print(result)  # Print the final converted numerical representation
