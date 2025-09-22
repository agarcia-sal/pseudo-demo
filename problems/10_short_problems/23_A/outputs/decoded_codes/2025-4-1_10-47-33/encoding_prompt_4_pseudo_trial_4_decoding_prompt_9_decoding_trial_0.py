# Begin the process to find the longest repeated substring length
line = input().strip()  # Read a line of input and remove trailing newline characters
n = len(line)  # Get the length of the input string
longest_repeated_length = 0  # Initialize the variable to keep track of the longest repeated length

# Iterate through possible lengths of substrings from 1 to n-1
for length in range(1, n):  
    # Check for repeated substrings of the current length
    for start_index in range(n - length):  # Limit start_index to ensure the substring fits
        # Extract the substring
        substring = line[start_index:start_index + length]

        # Check if the substring occurs again after the current index
        if substring in line[start_index + 1:]:  # Search in the remaining part of the string
            longest_repeated_length = length  # Update the longest repeated substring length
            break  # Break out of the inner loop to check for the next substring length

# Output the length of the longest repeated substring
print(longest_repeated_length)
