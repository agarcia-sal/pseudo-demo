# 1. Import Required Libraries
import sys

# 2. Read Input
input_string = input().strip()

# 3. Initialize Variables
index = 0
result = ""

# 4. Process the Input String
while index < len(input_string):
    if input_string[index] == '.':
        result += '0'
        index += 1
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'
        index += 2
    else:
        result += '2'
        index += 2

# 5. Output the Result
print(result)
