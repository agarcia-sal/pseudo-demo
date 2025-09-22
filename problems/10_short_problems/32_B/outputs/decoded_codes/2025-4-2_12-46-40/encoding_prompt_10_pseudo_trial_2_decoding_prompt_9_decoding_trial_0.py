# Start of the program

# Read a line of input and remove any surrounding whitespace
s = input().strip()

# Initialize index and answer variable
i = 0
ans = ''

# Loop through characters in the string until the end is reached
while i < len(s):
    # Check the current character for encoding
    if s[i] == '.':
        # If it's a single dot, append '0' to the answer
        ans += '0'
        i += 1
    elif i + 1 < len(s) and s[i + 1] == '.':
        # If next character is a dot, append '1' to the answer
        ans += '1'
        i += 2
    else:
        # In all other cases, append '2' to the answer
        ans += '2'
        i += 2

# Output the final result
print(ans)

# End of the program
