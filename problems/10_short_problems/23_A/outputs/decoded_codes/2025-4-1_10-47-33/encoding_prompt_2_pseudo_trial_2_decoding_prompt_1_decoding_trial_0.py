# Step 1: Read Input
input_line = input().strip()  # Obtain a line of text and remove trailing newline
lineLength = len(input_line)   # Determine the length of the input line

# Step 2: Initialize Variable
maxLength = 0  # Set a variable to track maximum length of substrings found

# Step 3: Outer Loop
for currentLength in range(lineLength):  # For each length from 0 to lineLength - 1
    # Step 3.1: Inner Loop
    for currentIndex in range(lineLength):  # For each character index in the input line
        # Step 3.2: Extract Substring
        subString = input_line[currentIndex:currentIndex + currentLength]  # Create the substring
        # Step 3.3: Check for Repetition
        if subString in input_line[currentIndex + 1:]:  # Check if substring occurs after currentIndex
            maxLength = currentLength  # Update maxLength if substring found
            break  # Exit inner loop since we found a repeated substring

# Step 4: Output Result
print(maxLength)  # Display the maximum length of the longest repeated substring found
