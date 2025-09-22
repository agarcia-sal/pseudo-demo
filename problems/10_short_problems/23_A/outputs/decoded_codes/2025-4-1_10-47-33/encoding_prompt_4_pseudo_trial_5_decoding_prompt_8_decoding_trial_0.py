# Read a line of input and remove the trailing newline character
line = input().strip()

# Determine the length of the input line
n = len(line)

# Initialize a variable to hold the result
repeatedLength = 0

# Loop through lengths of substrings from 0 to n-1
for length in range(n):
    # Check for substrings of the current length
    for startIndex in range(n - length):
        # Extract a substring from the current start index
        substring = line[startIndex:startIndex + length + 1]
        
        # Check if the substring occurs again later in the string
        if substring in line[startIndex + 1:]:
            # Update the result with the current length
            repeatedLength = length + 1
            break  # Exit inner loop if a repeat is found
            
# Output the length of the longest repeated substring
print(repeatedLength)


def longest_repeated_substring(line):
    line = line.strip()
    n = len(line)
    repeatedLength = 0
    # Logic as above
    return repeatedLength
