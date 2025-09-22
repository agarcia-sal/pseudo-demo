# Begin the program

# Read an input string from standard input
s = input().strip()  # Read input and remove whitespace from both ends

# Initialize index counter i and the answer string ans to empty
i = 0
ans = ""

# Loop until i reaches the length of s
while i < len(s):
    # Check if the current character is a dot
    if s[i] == '.':
        ans += '0'  # Append '0' to the answer string ans
        i += 1  # Move to the next character (i + 1)
    # Check if the next character is also a dot
    elif i + 1 < len(s) and s[i + 1] == '.':
        ans += '1'  # Append '1' to the answer string ans
        i += 2  # Move to the character after next (i + 2)
    else:
        ans += '2'  # Append '2' to the answer string ans
        i += 2  # Move to the character after next (i + 2)

# Output the final answer string
print(ans)

# End of the program
