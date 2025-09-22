# Begin the program

# Assume the input is a string consisting of characters '.' and other characters.

# Declare variables
s = input().strip()  # Read a line of input and remove any surrounding whitespace
i = 0  # Initialize index
ans = ''  # Initialize answer variable

# Loop through characters in the string until the end is reached
while i < len(s):
    # Check the current character for encoding
    if s[i] == '.':
        # If it's a single dot, append '0' to the answer
        ans += '0'
        i += 1  # Increment index by 1
    elif i + 1 < len(s) and s[i + 1] == '.':
        # If next character is a dot, append '1' to the answer
        ans += '1'
        i += 2  # Increment index by 2
    else:
        # In all other cases, append '2' to the answer
        ans += '2'
        i += 2  # Increment index by 2

# Output the final result
print(ans)

# End of the program
