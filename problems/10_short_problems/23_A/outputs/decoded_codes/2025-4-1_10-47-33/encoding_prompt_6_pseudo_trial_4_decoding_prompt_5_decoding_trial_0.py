# This function calculates the length of the longest repeated substring in a given input string
def find_longest_repetition_length():
    # Read a line of input
    string_line = input().strip()
    
    # Determine the length of the input line
    length_of_line = len(string_line)
    
    # Initialize a variable to store the result
    longest_repetition_length = 0
    
    # Loop over all possible lengths for repeated substrings
    for current_length in range(length_of_line):
        # Loop through the string to check for repeated substrings
        for start_index in range(length_of_line):
            # Extract the substring of the current length starting from start_index
            substring = string_line[start_index:start_index + current_length + 1]
            
            # Check if the substring appears again in the string after its starting index
            if substring in string_line[start_index + 1:]:
                # If found, update the longest repetition length
                longest_repetition_length = current_length + 1
                break  # Exit the inner loop to check a longer length
    
    # Output the length of the longest repeated substring
    print(longest_repetition_length)

# Example usage (uncomment to run):
# find_longest_repetition_length()
