# Read input string and strip leading/trailing whitespace
s = input().strip()

# Initialize the position index and the result string
index = 0
result = []

# Process the string according to given rules
while index < len(s):
    if s[index] == '.':
        # Current character is '.', append '0'
        result.append('0')
        index += 1
    elif (index + 1) < len(s) and s[index + 1] == '.':
        # Next character is '.', append '1' and move two steps
        result.append('1')
        index += 2
    else:
        # Neither current nor next character is '.', append '2' and move two steps
        result.append('2')
        index += 2

# Output the resulting string
print(''.join(result))
