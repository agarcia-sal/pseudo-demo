# Step 1: Read Input
line = input().strip()  # Read a line of text and remove trailing newline characters
lineLength = len(line)  # Get the length of the input line

# Step 2: Initialize Variable
maxLength = 0  # To track the maximum length of the substring found with repetitions

# Step 3: Outer Loop
for currentLength in range(lineLength):  # For each possible substring length
    # Step 3.1: Inner Loop
    for currentIndex in range(lineLength):  # For each character index within the input line
        # Step 3.1.1: Extract Substring
        subString = line[currentIndex:currentIndex + currentLength]  # Extract the substring

        # Step 3.1.2: Check for Repetition
        if subString and line.find(subString, currentIndex + 1) != -1:  # Look for the substring after currentIndex
            # Step 3.1.3: Update Maximum Length
            maxLength = currentLength  # Update maxLength to currentLength
            break  # Exit the inner loop if a repetition is found

# Step 4: Output Result
print(maxLength)  # Display the length of the longest repeated substring found
