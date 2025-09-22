# Read a line of input from the user
input_string = input().strip()

# Determine the length of the input line
length_of_line = len(input_string)

# Initialize a variable to store the length of the longest repeated substring
longest_repetition_length = 0

# Loop over all possible lengths for repeated substrings
for current_length in range(length_of_line):
    # Loop through the string to check for repeated substrings
    for start_index in range(length_of_line):
        # Extract the substring of the current length starting from start_index
        substring = input_string[start_index:start_index + current_length + 1]
        
        # Check if the substring appears again in the string after its starting index
        if substring in input_string[start_index + 1:]:
            # If found, update the longest repetition length
            longest_repetition_length = current_length + 1  # +1 because current_length is index
            break  # Exit the inner loop if a repetition is found

# Output the length of the longest repeated substring
print(longest_repetition_length)
