# Step 1: Read Input
line = input().strip()  # Read a line from input and remove any trailing newline characters
lengthOfLine = len(line)  # Store the length of the line

# Step 2: Initialize Variables
maxRepeatedLength = 0  # Variable to keep track of the maximum length of repeated substring

# Step 3: Outer Loop
for currentLength in range(1, lengthOfLine):  # Start from length 1 to lengthOfLine - 1
    found_repeat = False  # Flag to track if a repeated substring is found for the current length
    # Step 3.1: Inner Loop
    for startIndex in range(lengthOfLine - currentLength + 1):  # Valid start indices for the substrings
        # Extract the substring of the current length
        substring = line[startIndex:startIndex + currentLength]
        
        # Check if this substring appears again in line after startIndex
        if substring in line[startIndex + 1:]:
            maxRepeatedLength = currentLength  # Update maxRepeatedLength if a repeat is found
            found_repeat = True  # Set flag to true, indicating a repeat was found
            break  # No need to continue checking for more repeats of this length
    
    if found_repeat:  # If we found a repeat at any startIndex
        continue  # Continue to the next length

# Step 4: Output Result
print(maxRepeatedLength)  # Print the maximum length of the repeated substring
