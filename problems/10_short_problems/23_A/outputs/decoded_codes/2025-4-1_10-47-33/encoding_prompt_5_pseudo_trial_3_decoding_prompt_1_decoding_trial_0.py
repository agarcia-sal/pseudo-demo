# BEGIN

# Read a line of input from the user
line = input()

# Remove the newline character from the end of the input (not necessary in Python as input() does not include a newline)
line = line.rstrip('\n')

# Calculate the length of the input string
n = len(line)

# Initialize a variable to hold the length of the longest repeated substring
longestRepeatedLength = 0

# Loop through substrings of increasing lengths
for length in range(n):  # FOR length FROM 0 TO n - 1 DO
    # Check all starting positions for the substring of the current length
    for startPosition in range(n):  # FOR startPosition FROM 0 TO n - 1 DO
        
        # Extract the substring from 'startPosition' of 'length'
        currentSubstring = line[startPosition:startPosition + length]

        # Check if this substring appears again in the string after its starting position
        if currentSubstring and line.find(currentSubstring, startPosition + 1) != -1:  # IF condition
            # If the substring is found again, update the longest repeated length
            longestRepeatedLength = length
            break  # Exit this inner loop as we found a repeat

# Print the length of the longest repeated substring found
print(longestRepeatedLength)

# END
