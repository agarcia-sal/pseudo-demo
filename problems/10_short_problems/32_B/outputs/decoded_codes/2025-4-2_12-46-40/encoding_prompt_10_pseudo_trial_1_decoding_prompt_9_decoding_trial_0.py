# Begin program

# Read a string input
s = input()
i = 0
ans = ""

# Loop through each character of the string 's'
while i < len(s):
    # Check for a single dot
    if s[i] == '.':
        ans += '0'  # Append '0' to ans for a single dot
        i += 1  # Increment index by 1
    else:
        # Check next character for a dot
        if i + 1 < len(s) and s[i + 1] == '.':
            ans += '1'  # Append '1' to ans for a dot followed by a dot
            i += 2  # Increment index by 2
        else:
            ans += '2'  # Append '2' to ans for a non-dot situation
            i += 2  # Increment index by 2

# Output the final result
print(ans)

# End program
