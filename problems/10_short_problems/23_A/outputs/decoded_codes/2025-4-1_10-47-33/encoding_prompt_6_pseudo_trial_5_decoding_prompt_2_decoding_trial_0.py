# Begin program to find the longest repeating substring length

# 1. Read a line of input and remove the last character (newline).
input_line = input().rstrip('\n')

# 2. Store the length of the input line in a variable called totalLength.
totalLength = len(input_line)

# 3. Initialize a variable longestRepeatLength to 0 to track the length of the longest repeating substring.
longestRepeatLength = 0

# 4. Loop through possible substring lengths from 0 to totalLength
for length in range(totalLength + 1):
    # a. Loop through each starting index from 0 to totalLength
    for start in range(totalLength + 1):
        # i. Extract a substring starting from the current index with the current length.
        substring = input_line[start:start + length]
        
        # ii. Check if this substring appears again in the input, starting from the position after the current index.
        if substring in input_line[start + 1:]:
            # iii. If found, set longestRepeatLength to the current length.
            longestRepeatLength = length
            
            # iv. Break out of the inner loop as we found a repeating substring of the current length.
            break

# 5. Print longestRepeatLength
print(longestRepeatLength)
