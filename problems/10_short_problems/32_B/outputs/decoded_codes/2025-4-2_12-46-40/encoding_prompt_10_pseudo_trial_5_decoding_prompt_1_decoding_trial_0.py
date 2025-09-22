# Import necessary functions (assumed action)
# Assume input is provided through standard input stream

s = input()                         # Read input from the user
s = s.strip()                      # Strip whitespace from s

i = 0                               # Initialize index counter i to 0
ans = ""                            # Initialize the answer string ans to empty

while i < len(s):                  # Loop until i reaches the length of s
    if s[i] == '.':                # Check if the current character is a dot
        ans += '0'                 # Append '0' to the answer string ans
        i += 1                     # Move to the next character (i + 1)
    elif i + 1 < len(s) and s[i + 1] == '.':  # Check if the next character is also a dot
        ans += '1'                 # Append '1' to the answer string ans
        i += 2                     # Move to the character after next (i + 2)
    else:                          # If neither of the above conditions are true
        ans += '2'                 # Append '2' to the answer string ans
        i += 2                     # Move to the character after next (i + 2)

print(ans)                         # Output the final answer string
