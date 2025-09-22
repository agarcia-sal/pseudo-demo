# Start the program

# Read the input string and remove any leading or trailing whitespace
inputString = input().strip()

# Initialize a variable named `index` to `0`
index = 0

# Initialize an empty string named `result` to build the output
result = ""

# While the current index is less than the length of the input string:
while index < len(inputString):
    # If the character at the current index is a period ('.'):
    if inputString[index] == '.':
        # Append '0' to the `result` string
        result += '0'
        # Move to the next character by increasing `index` by `1`
        index += 1
        
    # Else, if the character at the position after the current index is a period ('.'):
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to the `result` string
        result += '1'
        # Move ahead by two characters by increasing `index` by `2`
        index += 2
        
    # Otherwise:
    else:
        # Append '2' to the `result` string
        result += '2'
        # Move ahead by two characters by increasing `index` by `2`
        index += 2

# After finishing the loop, output the `result` string
print(result)
