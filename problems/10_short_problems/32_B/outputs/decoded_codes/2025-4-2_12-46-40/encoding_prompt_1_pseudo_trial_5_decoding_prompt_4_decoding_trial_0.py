# Read a line of input from the user and remove any extra whitespace
s = input().strip()

# Initialize an index to track position in the string
index = 0

# Initialize an empty string to store the result
result = ""

# Loop through the input string until the end
while index < len(s):
    
    # Check if the current character is a dot
    if s[index] == '.':
        # Append '0' to the result
        result += '0'
        # Move to the next character
        index += 1
    
    # Check if the next character is a dot
    elif index + 1 < len(s) and s[index + 1] == '.':
        # Append '1' to the result
        result += '1'
        # Skip the next character
        index += 2
    
    # Handle the case where the current character is not a dot and the next character is not a dot
    else:
        # Append '2' to the result
        result += '2'
        # Skip the next character
        index += 2

# Output the final result
print(result)
