# Start of the program
# Read input string from standard input
s = input()

# Initialize index and result string
index = 0
result = ''

# Loop until all characters in the string have been processed
while index < len(s):
    # Check if the current character is a single dot
    if s[index] == '.':
        # Append '0' to the result for a single dot
        result += '0'
        index += 1  # Move to the next character
        
    # Check if the next character is also a dot
    elif index + 1 < len(s) and s[index + 1] == '.':
        # Append '1' to the result for two consecutive dots
        result += '1'
        index += 2  # Move past both dots
        
    else:
        # Append '2' for any other scenario (dot followed by something else)
        result += '2'
        index += 2  # Move past both characters

# Output the result string
print(result)

# End of the program
