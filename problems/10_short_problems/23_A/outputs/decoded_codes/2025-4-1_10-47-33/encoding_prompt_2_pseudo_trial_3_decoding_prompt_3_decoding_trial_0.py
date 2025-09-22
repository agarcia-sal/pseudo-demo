# Function to find the length of the longest repeating substring
def longest_repeating_substring():
    # Step 1: Input - Read a line of text
    line = input().strip()
    
    # Step 2: Initialize variables
    textLength = len(line)
    maximumLength = 0  # To track the longest repeating substring length

    # Step 3: Outer loop for each possible substring length
    for currentLength in range(1, textLength):  # Start from 1 to avoid empty substring
        # Inner loop for each starting position
        for startPosition in range(textLength - currentLength):
            # Extract the substring
            substring = line[startPosition:startPosition + currentLength]

            # Check if the substring appears again in the remaining part of the line
            if substring in line[startPosition + currentLength:]:
                # Update maximumLength and move to the next length
                maximumLength = currentLength
                break  # Exit inner loop on first valid repetition found

    # Step 4: Output the maximum length of the repeating substring
    print(maximumLength)

# Call the function to execute
longest_repeating_substring()
