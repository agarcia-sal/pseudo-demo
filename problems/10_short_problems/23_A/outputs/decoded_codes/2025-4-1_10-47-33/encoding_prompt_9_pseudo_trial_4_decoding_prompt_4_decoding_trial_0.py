# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Receive input
    line = input().rstrip('\n')
    line_length = len(line)

    # Initialize the counter for the longest repeated substring length
    longest_repeated_substring_length = 0

    # Iterate over possible substring lengths
    for current_length in range(1, line_length):
        # Inner loop to check each starting index
        for start_index in range(line_length - current_length + 1):
            # Extract the substring
            substring = line[start_index:start_index + current_length]
            
            # Check if this substring appears later in the line
            if substring in line[start_index + current_length:]:
                # Update the longest length found
                longest_repeated_substring_length = current_length
                # Break out of inner loop as we found a repeated substring
                break

    # Output the result
    print(longest_repeated_substring_length)

# Call the function to execute the code
longest_repeated_substring()
