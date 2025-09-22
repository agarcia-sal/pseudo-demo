# Begin the program

# Read input string from standard input
input_string = input()

# Initialize index and result string
index = 0
result = ''

# Loop until all characters in the string have been processed
while index < len(input_string):
    # Check if the current character is a dot
    if input_string[index] == '.':
        # Append '0' to the result for a single dot
        result += '0'
        # Increment index by 1
        index += 1
        
    # Check if the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # Append '1' to the result for a dot followed by a dot
        result += '1'
        # Increment index by 2
        index += 2
        
    else:
        # Append '2' for any other scenario (dot followed by something else)
        result += '2'
        # Increment index by 2
        index += 2

# Output the result string
print(result)

# End of program
