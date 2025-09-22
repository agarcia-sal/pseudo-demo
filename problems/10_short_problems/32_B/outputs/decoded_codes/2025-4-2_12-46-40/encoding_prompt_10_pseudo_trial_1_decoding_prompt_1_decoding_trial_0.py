# BEGIN PROGRAM

# Define input assumptions
s = input()  # Read the input string from standard input
i = 0  # Initialize 'i' as 0
ans = ""  # Initialize 'ans' as an empty string

# Loop through each character of the string 's'
while i < len(s):  # WHILE i is less than the length of 's' DO
    # Check for a single dot
    if s[i] == '.':  # IF s[i] is equal to '.' THEN
        ans += '0'  # APPEND '0' to 'ans'
        i += 1  # INCREMENT i by 1
    else:
        # Check next character for a dot
        if i + 1 < len(s) and s[i + 1] == '.':  # IF s[i + 1] is equal to '.' THEN
            ans += '1'  # APPEND '1' to 'ans'
            i += 2  # INCREMENT i by 2
        else:
            ans += '2'  # APPEND '2' to 'ans'
            i += 2  # INCREMENT i by 2

# Output the final result
print(ans)  # PRINT ans

# END PROGRAM
