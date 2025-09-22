# Step 1: Input the line of text and strip the newline character
line = input().strip()

# Step 2: Initialize necessary variables
textLength = len(line)  # Determine the length of the line
maximumLength = 0  # Initialize the variable to track the maximum length found

# Step 3: Outer Loop for each possible length of substring
for currentLength in range(1, textLength):  # Start from 1 to avoid empty substring
    # Step 3.1: Inner Loop for each starting position in the line
    for startPosition in range(textLength - currentLength + 1):  # Ensure substring does not go out of bounds
        # Extract the current substring
        substring = line[startPosition:startPosition + currentLength]
        
        # Check if the substring appears again in the line
        # We check from startPosition + 1 to allow non-overlapping
        if substring in line[startPosition + 1:]:
            maximumLength = currentLength  # Update maximumLength
            break  # Exit the inner loop since only the first repetition matters

# Step 4: Output the maximum length found
print(maximumLength)
