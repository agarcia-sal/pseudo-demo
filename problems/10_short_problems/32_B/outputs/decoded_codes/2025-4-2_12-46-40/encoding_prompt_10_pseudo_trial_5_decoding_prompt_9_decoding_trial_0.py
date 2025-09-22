# Import necessary functions (assumed action)
# Assume input is provided through standard input stream

# Read input from user
s = input()  
# Strip whitespace from s
s = s.strip()  

# Initialize index counter i to 0
i = 0  
# Initialize the answer string ans to empty
ans = ''  

# Loop until i reaches the length of s
while i < len(s):
    # Check if the current character is a dot
    if s[i] == '.':
        # Append '0' to the answer string ans
        ans += '0'
        # Move to the next character (i + 1)
        i += 1  
    # Check if the next character is also a dot
    elif i + 1 < len(s) and s[i + 1] == '.':
        # Append '1' to the answer string ans
        ans += '1'
        # Move to the character after next (i + 2)
        i += 2  
    else:
        # Append '2' to the answer string ans
        ans += '2'
        # Move to the character after next (i + 2)
        i += 2  

# Output the final answer string
print(ans)  
