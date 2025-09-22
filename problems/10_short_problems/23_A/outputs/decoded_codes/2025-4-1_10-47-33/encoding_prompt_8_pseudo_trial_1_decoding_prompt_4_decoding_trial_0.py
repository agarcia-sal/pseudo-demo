def longest_repeated_substring_length(input_line):
    # Get the length of the input string
    length_of_input = len(input_line)
    longest_repeated_length = 0
    
    # Loop through all possible substring lengths from 1 to (length of input)
    for substring_length in range(1, length_of_input):
        # Loop through all starting positions of the substring in the input
        for start_index in range(length_of_input - substring_length + 1):
            # Extract the current substring
            current_substring = input_line[start_index:start_index + substring_length]
            
            # Check if the current substring appears again in the input after its starting position
            if current_substring in input_line[start_index + substring_length:]:
                # Update the length of the longest repeated substring found
                longest_repeated_length = substring_length
    
    return longest_repeated_length

# Read input
input_line = input().strip()  # Strip trailing newline character
# Get the length of the longest repeated substring
result = longest_repeated_substring_length(input_line)
# Output the result
print(result)
