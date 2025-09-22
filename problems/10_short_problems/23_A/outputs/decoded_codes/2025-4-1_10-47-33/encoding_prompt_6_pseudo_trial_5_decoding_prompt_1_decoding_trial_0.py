# Begin program to find the longest repeating substring length
input_line = input().rstrip()  # Read a line of input and remove the last character (newline)
totalLength = len(input_line)  # Store the length of the input line
longestRepeatLength = 0  # Initialize the longest repeating substring length

# Loop through possible substring lengths from 0 to totalLength
for length in range(totalLength + 1):  # For each length from 0 to totalLength (inclusive)
    for start_index in range(totalLength + 1):  # Loop through each starting index
        substring = input_line[start_index:start_index + length]  # Extract the substring
        if substring in input_line[start_index + length:]:  # Check if it appears again after current index
            longestRepeatLength = length  # Update the longest repeating length
            break  # Break out of the inner loop as we found a repeating substring

# After checking all lengths, output the longest found repeating substring length
print(longestRepeatLength)  # Print the longest repeating substring length
