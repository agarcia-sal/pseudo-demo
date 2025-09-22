# Begin the translation of the pseudocode into Python

# Read input from standard input
s = input()

# Initialize index and result variable
index = 0
output = ""  # This will hold the transformed output string

# Process the input string
while index < len(s):
    if s[index] == '.':
        # Current character is '.', map it to '0'
        output += '0'  # Append '0' to output
        index += 1  # Increment index by 1
    elif index + 1 < len(s) and s[index + 1] == '.':
        # Next character is also '.', map the current to '1'
        output += '1'  # Append '1' to output
        index += 2  # Increment index by 2
    else:
        # Neither of the two characters is '.', map it to '2'
        output += '2'  # Append '2' to output
        index += 2  # Increment index by 2

# Display the result
print(output)
