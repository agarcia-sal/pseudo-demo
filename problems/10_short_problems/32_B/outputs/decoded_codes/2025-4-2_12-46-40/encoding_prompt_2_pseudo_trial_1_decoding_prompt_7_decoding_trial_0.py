# Step 1: Read a line of input
inputString = input().strip()  # Remove leading/trailing whitespace

# Step 2: Initialize index and result
index = 0
result = ""  # String to hold the final output

# Step 3: Loop through the input string as long as our index is less than its length
while index < len(inputString):
    # Step 4: Check the current character
    if inputString[index] == '.':
        result += '0'  # Append '0' for a single dot
        index += 1     # Move to the next character

    else:
        # Check the next character if it exists
        if index + 1 < len(inputString) and inputString[index + 1] == '.':
            result += '1'  # Two consecutive dots found, append '1'
            index += 2     # Move forward by two characters

        else:
            result += '2'  # Not followed by a dot, append '2'
            index += 2     # Move forward by two characters

# Step 5: Output the result
print(result)
