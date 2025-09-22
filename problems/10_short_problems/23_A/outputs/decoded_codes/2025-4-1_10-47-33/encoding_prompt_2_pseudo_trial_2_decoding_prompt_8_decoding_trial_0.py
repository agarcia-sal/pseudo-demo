# Step 1: Read Input
line = input().rstrip()  # Read a line of text and remove the trailing newline character
lineLength = len(line)   # Get the length of the input line

# Step 2: Initialize Variable
maxLength = 0  # Track the maximum length of the substring found with repetitions

# Step 3: Outer Loop
for currentLength in range(lineLength):  # Loop through each possible substring length
    # Step 3.1: Inner Loop
    for currentIndex in range(lineLength):  # Loop through each character index
        # Step 3.1.1: Extract Substring
        subString = line[currentIndex:currentIndex + currentLength]  # Create the substring
        
        # Step 3.1.2: Check for Repetition
        if line.find(subString, currentIndex + 1) != -1:  # Look for occurrence after currentIndex
            # Step 3.1.3: Update Maximum Length
            maxLength = currentLength + 1  # Update maxLength
            break  # Exit the inner loop if a repeat is found

# Step 4: Output Result
print(maxLength)  # Display the length of the longest repeated substring found
