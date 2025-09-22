# Initialize Program
inputLine = input().strip()  # Read a line of input and remove trailing newline characters
length = len(inputLine)       # Store the length of the input line
result = 0                    # Initialize result to 0

# Main Loop
for subLength in range(length):  # For each possible substring length from 0 to length - 1
    for startIndex in range(length):  # For each starting position from 0 to length - 1
        substring = inputLine[startIndex:startIndex + subLength]  # Extract the substring
        
        # Check if the substring appears again in inputLine starting from startIndex + 1
        if substring in inputLine[startIndex + 1:]:
            result = subLength  # Update result to be the current subLength
            break  # Break out of the inner loop to test the next substring length

# Output the Result
print(result)  # Print the value of result
