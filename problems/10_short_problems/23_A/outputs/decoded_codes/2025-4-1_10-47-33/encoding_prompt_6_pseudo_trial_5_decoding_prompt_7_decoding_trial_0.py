# Begin program to find the longest repeating substring length

# Step 1: Read a line of input and remove the last character (newline).
input_line = input().strip()

# Step 2: Store the length of the input line in a variable called totalLength.
totalLength = len(input_line)

# Step 3: Initialize a variable longestRepeatLength to 0 to track the length of the longest repeating substring.
longestRepeatLength = 0

# Step 4: Loop through possible substring lengths from 1 to totalLength (starting from 1 makes sense for lengths)
for length in range(1, totalLength + 1):
    # Step 4a: Loop through each starting index from 0 to totalLength - length (to prevent out-of-bounds)
    for start in range(totalLength - length + 1):
        # Step 4ai: Extract a substring starting from the current index with the current length.
        substring = input_line[start:start + length]
        
        # Step 4aii: Check if this substring appears again in the input, 
        # starting from the position after the current index.
        if substring in input_line[start + 1:]:
            # Step 4aiii: If found, set longestRepeatLength to the current length.
            longestRepeatLength = length
            # Step 4aiv: Break out of the inner loop as we found a repeating substring of the current length.
            break

# Step 5: After checking all lengths, output the longest found repeating substring length
print(longestRepeatLength)
