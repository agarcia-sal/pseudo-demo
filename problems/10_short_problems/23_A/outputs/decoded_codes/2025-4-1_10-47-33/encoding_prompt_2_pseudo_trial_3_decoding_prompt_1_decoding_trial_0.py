# Step 1: Input
line = input().strip()  # Read a line of text, excluding newline character

# Step 2: Initialize
textLength = len(line)  # Determine the length of the line of text
maximumLength = 0  # Initialize maximumLength to zero

# Step 3: Outer Loop
for currentLength in range(textLength):  # For each possible length of substring
    # Step 3: Inner Loop
    for startPosition in range(textLength):  # For each starting position
        substring = line[startPosition:startPosition + currentLength]  # Extract the substring
        if substring in line[startPosition + currentLength:]:  # Check for repetitions
            maximumLength = currentLength  # Update maximumLength
            break  # Exit the inner loop if a repetition is found

# Step 4: Output
print(maximumLength)  # Print the value of maximumLength
