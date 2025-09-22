# BEGIN PROGRAM

# Read a line of input
line = input().rstrip()  # Removing newline character
lineLength = len(line)    # Get the length of the line
resultValue = 0           # Initialize result value

# Loop through all possible substring lengths from 0 to lineLength - 1
for l in range(lineLength):  # `range(lineLength)` goes from 0 to lineLength - 1
    
    # Loop through each index in the line to check for repeated substrings
    for i in range(lineLength):  # `range(lineLength)` goes from 0 to lineLength - 1
        
        # Extract a substring of length l starting from current index i
        substring = line[i:i+l]  # Get substring from index `i` of length `l`
        
        # Check if this substring occurs again later in the line
        if substring in line[i+1:]:  # Check if substring exists starting from `i + 1`
            resultValue = l  # Update the resultValue to the current length l
            break  # Break out of inner loop
          
# Output the maximum length of the found repeated substring
print(resultValue)  # Print the result value

# END PROGRAM
