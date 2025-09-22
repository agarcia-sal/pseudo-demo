# Step 1: Read a line of input and remove any leading/trailing whitespace.
inputString = input().strip()

# Step 2: Initialize a variable `index` to 0.
index = 0

# Step 3: Initialize an empty string `result`.
result = ""

# Step 4: While `index` is less than the length of `inputString`:
while index < len(inputString):
    # If the current character is a dot ('.'):
    if inputString[index] == '.':
        # Append the character '0' to `result`.
        result += '0'
        # Move to the next character.
        index += 1
    
    # Otherwise, check the character immediately following the current character.
    else:
        # Check if the following character is also a dot ('.'):
        if index + 1 < len(inputString) and inputString[index + 1] == '.':
            # Append the character '1' to `result`.
            result += '1'
            # Move forward by two characters.
            index += 2
        
        # If the following character is not a dot:
        else:
            # Append the character '2' to `result`.
            result += '2'
            # Move forward by two characters.
            index += 2

# Step 5: After processing all characters, output the final `result`.
print(result)
