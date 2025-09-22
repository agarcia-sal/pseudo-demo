# Step 1: Read input and strip whitespace
inputString = input().strip()

# Step 2: Initialize index and result
index = 0
result = ""

# Step 4: Loop through the input string based on index
while index < len(inputString):
    # Check if the current character is a dot
    if inputString[index] == '.':
        result += '0'
        index += 1  # Move to the next character
    else:
        # Check the next character if there is one
        if index + 1 < len(inputString):
            if inputString[index + 1] == '.':
                result += '1'
                index += 2  # Move forward by two characters
            else:
                result += '2'
                index += 2  # Move forward by two characters
        else:
            # If there's no following character, handle as needed (could be an edge case)
            result += '2'
            index += 1  # Just move one character ahead

# Step 5: Output the final result
print(result)
