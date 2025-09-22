# Step 1: Define Input Source
s = input().strip()

# Step 2: Initialize Variables
current_position = 0
result = ""

# Step 3: Process the Input String
while current_position < len(s):
    if s[current_position] == '.':
        result += '0'
        current_position += 1
    elif current_position + 1 < len(s) and s[current_position + 1] == '.':
        result += '1'
        current_position += 2
    else:
        result += '2'
        current_position += 2

# Step 4: Output the Result
print(result)
