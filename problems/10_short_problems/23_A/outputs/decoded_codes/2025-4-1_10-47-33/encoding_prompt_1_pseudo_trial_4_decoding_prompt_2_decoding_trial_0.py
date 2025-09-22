# Initialize Program
inputLine = input().strip()  # Read input and remove trailing newline
length = len(inputLine)  # Store length of the input line
result = 0  # Initialize result to 0

# Main Loop
for subLength in range(length):  # For each possible substring length from 0 to length - 1
    for startIndex in range(length):  # For each starting position from 0 to length - 1
        substring = inputLine[startIndex:startIndex + subLength]  # Extract the substring
        if substring in inputLine[startIndex + 1:]:  # Check if substring appears again
            result = subLength  # Update result to current subLength
            break  # Break out of the inner loop to test the next substring length

# Output the Result
print(result)  # Print the length of the longest repeating substring
