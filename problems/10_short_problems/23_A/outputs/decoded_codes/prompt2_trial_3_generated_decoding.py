# Step 1: Read a line of input and remove the last character
line = input()[:-1]

# Step 2: Determine the length of the line
lengthOfLine = len(line)

# Step 3: Initialize the variable for the length of the longest repeated substring
repeatedSubstringLength = 0

# Step 4: Loop over possible lengths of substrings
for substringLength in range(lengthOfLine):
    # Step 4.1: Loop through each index in the line
    for i in range(lengthOfLine):
        # Step 4.1.1: Extract the substring of current length
        substring = line[i:i + substringLength + 1]  # +1 because range is exclusive

        # Step 4.1.2: Check if the substring occurs again later in the line
        if substring in line[i + 1:]:
            # Step 4.1.3: Update the length of the longest repeated substring
            repeatedSubstringLength = substringLength + 1  # +1 for the actual length of the substring
            break  # Exit the inner loop to check the next substring length

# Step 5: Output the length of the longest repeated substring
print(repeatedSubstringLength)
