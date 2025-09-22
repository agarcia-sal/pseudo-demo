# Step 1: Input
line = input().strip()

# Step 2: Initialize
textLength = len(line)
maximumLength = 0

# Step 3: Outer Loop
for currentLength in range(1, textLength):  # Start from 1 to avoid empty substring
    # Inner Loop
    for startPosition in range(textLength - currentLength):
        substring = line[startPosition:startPosition + currentLength]
        # Check if substring appears again
        if substring in line[startPosition + currentLength:]:
            maximumLength = currentLength
            break  # Found a repetition, exit inner loop

# Step 4: Output
print(maximumLength)
