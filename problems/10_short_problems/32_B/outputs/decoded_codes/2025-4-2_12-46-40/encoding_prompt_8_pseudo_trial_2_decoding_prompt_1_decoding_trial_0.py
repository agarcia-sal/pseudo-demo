# Step 1: Start (implicit in Python)

# Step 2: Read Input
input_string = input().strip()

# Step 3: Initialize Variables
index = 0
result = ""

# Step 4: Process the String
while index < len(input_string):
    if input_string[index] == '.':
        result += '0'
        index += 1  # Move to next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'
        index += 2  # Move past the two symbols
    else:
        result += '2'
        index += 2  # Move past the two symbols

# Step 5: Output Result
print(result)

# Step 6: End (implicit in Python)
