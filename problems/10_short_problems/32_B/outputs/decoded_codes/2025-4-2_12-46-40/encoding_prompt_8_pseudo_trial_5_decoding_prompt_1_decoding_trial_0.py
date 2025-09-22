# 1. Import Required Libraries
import sys

# 2. Read Input
input_string = input().strip()

# 3. Initialize Variables
index = 0
result = ""

# 4. Process the Input String
while index < len(input_string):
    # If the current character (at index) is a dot ('.'):
    if input_string[index] == '.':
        result += '0'
        index += 1
    # Else, if the next character (at index + 1) is also a dot ('.'):
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'
        index += 2  # Move forward by 2, skip both characters
    # Otherwise:
    else:
        result += '2'
        index += 2  # Move forward by 2, skip both characters

# 5. Output the Result
print(result)
