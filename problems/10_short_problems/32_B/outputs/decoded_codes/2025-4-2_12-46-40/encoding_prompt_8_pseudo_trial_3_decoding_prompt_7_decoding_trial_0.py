# Step 1: Define Input Source
# Read a line of input and strip any leading or trailing whitespace
input_string = input().strip()

# Step 2: Initialize Variables
# This represents our current position in the input string
current_position = 0
# This will hold the final output as a string
result = ""

# Step 3: Process the Input String
# Loop through the input string until reaching the end
while current_position < len(input_string):
    # Check if the current character is a dot
    if input_string[current_position] == '.':
        result += '0'  # Add '0' to the result for a single dot
        current_position += 1  # Move to the next character
    
    # Check if there is a next character and it is also a dot
    elif (current_position + 1 < len(input_string) and 
          input_string[current_position + 1] == '.'):
        result += '1'  # Add '1' to the result for two consecutive dots
        current_position += 2  # Move ahead by 2 positions
    
    # If the conditions for single or double dots aren't met, add '2'
    else:
        result += '2'  # For any other character configuration
        current_position += 2  # Move ahead by 2 positions

# Step 4: Output the Result
# Print the final result which contains the converted numerical representation
print(result)
