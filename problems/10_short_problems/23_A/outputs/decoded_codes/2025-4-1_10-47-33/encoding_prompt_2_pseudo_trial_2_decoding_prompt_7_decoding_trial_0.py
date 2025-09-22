# Step 1: Read Input
line = input()  # Obtain a line of text from standard input
lineLength = len(line)  # Determine the length of the input line

# Step 2: Initialize Variable
maxLength = 0  # This will track the maximum length of the substring found with repetitions

# Step 3: Outer Loop
for currentLength in range(1, lineLength):  # Starting from 1 up to lineLength (exclusive)
    # Step 3.1: Inner Loop
    for currentIndex in range(lineLength):  # For each character index within the range of lineLength
        # Step 3.1.1: Extract Substring
        subString = line[currentIndex:currentIndex + currentLength]  # Create a substring
        
        # Step 3.1.2: Check for Repetition
        if line.find(subString, currentIndex + 1) != -1:  # Look for the occurrence after currentIndex
            # Step 3.1.3: Update Maximum Length
            maxLength = currentLength  # Update maxLength to currentLength
            break  # Exit the inner loop as we found a repetition

# Step 4: Output Result
print(maxLength)  # Display the value of maxLength
