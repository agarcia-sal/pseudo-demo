# Begin program

# Read a line of input from the standard input
input_string = input()

# Initialize a starting index for the loop
index = 0

# Initialize an empty string for the output answer
output_string = ''

# Loop until the index reaches the length of input_string
while index < len(input_string):
    # Check if the current character is a dot
    if input_string[index] == '.':
        # Append '0' to the output string
        output_string += '0'
        # Move to the next character
        index += 1
    
    # Check if the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # Append '1' to the output string
        output_string += '1'
        # Skip the next character as it forms a pair
        index += 2
    
    # If neither condition is true, it means we have a dash
    else:
        # Append '2' to the output string
        output_string += '2'
        # Skip the next character as it forms a pair
        index += 2

# Output the final string
print(output_string)

# End program
