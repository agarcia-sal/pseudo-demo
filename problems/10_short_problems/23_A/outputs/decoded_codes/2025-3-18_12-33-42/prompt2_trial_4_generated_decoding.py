# Step 1: Read a line of text from standard input, removing the trailing newline character
input_line = input().strip()

# Step 2: Determine the length of the input line and store it in a variable called inputLength
inputLength = len(input_line)

# Step 3: Initialize a variable called repeatedLength to 0
repeatedLength = 0

# Step 4: Loop through all possible lengths of substrings from 0 to inputLength - 1
for currentLength in range(inputLength):
    # Step 4.1: Loop through all starting positions in the input line
    for startIndex in range(inputLength - currentLength):
        # Step 4.1.1: Extract the substring of length currentLength starting at startIndex
        substring = input_line[startIndex:startIndex + currentLength + 1]
        
        # Step 4.1.2: Check if the substring appears again in the remainder of the input line
        if substring in input_line[startIndex + 1:]:
            # Step 4.1.3: Update the repeatedLength if the substring is found
            repeatedLength = currentLength + 1
            break  # Exit the inner loop as we are only interested in the longest length

# Step 5: Output the value of repeatedLength
print(repeatedLength)
