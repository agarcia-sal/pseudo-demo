# BEGIN PROGRAM

# Read a line of input
line = input()  # Input from standard input
lineLength = len(line)  # Calculate the length of the line
resultValue = 0  # Initialize resultValue to 0

# Loop through all possible substring lengths from 0 to lineLength - 1
for l in range(lineLength):  # l iterates from 0 to lineLength - 1
    # Loop through each index in the line
    for i in range(lineLength):  # i iterates from 0 to lineLength - 1
        # Extract a substring of length l starting from current index i
        substring = line[i:i + l]  # Substring from index i for length l

        # Check if this substring occurs again later in the line
        if substring in line[i + 1:]:  # Check existence in the rest of the line
            resultValue = l  # Update the resultValue to the current length l
            break  # Exit the inner loop

# Output the maximum length of the found repeated substring
print(resultValue)  # Output resultValue

# END PROGRAM
