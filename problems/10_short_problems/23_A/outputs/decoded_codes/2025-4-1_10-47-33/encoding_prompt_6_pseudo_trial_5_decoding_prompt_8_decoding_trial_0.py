# Begin program to find the longest repeating substring length
input_line = input().rstrip('\n')  # Read input and remove the last newline
totalLength = len(input_line)  # Store the length of the input line
longestRepeatLength = 0  # Initialize variable to track the length of the longest repeating substring

# Loop through possible substring lengths from 0 to totalLength
for length in range(totalLength + 1):  # For each length from 0 to totalLength (inclusive)
    for start in range(totalLength + 1):  # Loop through each starting index from 0 to totalLength
        substring = input_line[start:start + length]  # Extract substring
        if substring and input_line.find(substring, start + 1) != -1:  # Check if substring appears again
            longestRepeatLength = length  # Set longestRepeatLength to current length
            break  # Break out of the inner loop

# After checking all lengths, output the longest found repeating substring length
print(longestRepeatLength)
