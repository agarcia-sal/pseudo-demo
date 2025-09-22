# Begin program definition

# Read input string
s = input()

# Initialize index and output string
i = 0
ans = ""

# Loop through each character of the string 's'
while i < len(s):
    # Check for a single dot
    if s[i] == '.':
        ans += '0'  # Append '0' to output for single dot
        i += 1      # Move to the next character
    else:
        # Check next character for a dot
        if (i + 1) < len(s) and s[i + 1] == '.':
            ans += '1'  # Append '1' if next character is a dot
            i += 2      # Move two characters ahead
        else:
            ans += '2'  # Append '2' for a non-dot character
            i += 2      # Move two characters ahead

# Output the final result
print(ans)

# End program
