# Start the Program

# Read Input: Receive a single line of input, trim whitespace
inputString = input().strip()

# Initialize Variables: Set a counter `index` and create an empty result string
index = 0
result = ""

# Process the Input String: While `index` is less than the length of `inputString`
while index < len(inputString):
    # If the character at the current `index` is a dot (`.`)
    if inputString[index] == '.':
        result += '0'  # Append '0' to `result`
        index += 1  # Increment `index` by 1 to move to the next character
    # Else If the character at the next `index` is also a dot (`.`)
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        result += '1'  # Append '1' to `result`
        index += 2  # Increment `index` by 2 to skip the next character
    # Else: Any character that is not a dot
    else:
        result += '2'  # Append '2' to `result`
        index += 2  # Increment `index` by 2 to skip the next character

# Output the Result: Print the final value of `result`
print(result)
