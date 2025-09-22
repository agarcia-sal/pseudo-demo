# This program reads a string input and translates it based on certain character rules.
# The input is processed character by character, appending values to an output string.

# Read a line of input and remove any surrounding whitespace
s = input().strip()  # Read input and strip whitespace

# Initialize index and answer variable
i = 0
ans = ''  # This will store our output

# Loop through characters in the string until the end is reached
while i < len(s):
    # Check the current character for encoding
    if s[i] == '.':
        # If it's a single dot, append '0' to the answer
        ans += '0'  # Append '0' for single dot
        i += 1  # Move to the next character
    elif i + 1 < len(s) and s[i + 1] == '.':
        # If the next character is a dot, append '1' to the answer
        ans += '1'  # Append '1' for dot followed by dot
        i += 2  # Move past both dots
    else:
        # In all other cases, append '2' to the answer
        ans += '2'  # Append '2' for any other character
        i += 2  # Move past the current character

# Output the final result
print(ans)  # Print the accumulated answer
