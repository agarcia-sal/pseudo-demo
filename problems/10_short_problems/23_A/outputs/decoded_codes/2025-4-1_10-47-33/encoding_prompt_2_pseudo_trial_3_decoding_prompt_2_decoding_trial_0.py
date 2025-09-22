# Step 1: Input
line = input().rstrip()  # Read a line of text and remove the newline character

# Step 2: Initialize variables
textLength = len(line)  # Get the length of the line
maximumLength = 0       # Initialize the maximum length of the repeating substring to zero

# Step 3: Outer Loop for each possible length of substring
for currentLength in range(textLength):  # currentLength goes from 0 to textLength - 1
    # Step 3.1: Inner Loop for each starting position
    for startPosition in range(textLength):  # startPosition goes from 0 to textLength - 1
        substring = line[startPosition:startPosition + currentLength]  # Extract the substring
        
        # Ensure we only check if the length of the substring is valid
        if substring and (startPosition + currentLength < textLength):
            # Step 3.2: Check for repetition of the substring
            if substring in line[startPosition + currentLength:]:  # Check if the substring appears later in the string
                maximumLength = currentLength  # Update maximumLength to the current substring length
                break  # Exit inner loop after finding the first valid repetition

# Step 4: Output the result
print(maximumLength)
