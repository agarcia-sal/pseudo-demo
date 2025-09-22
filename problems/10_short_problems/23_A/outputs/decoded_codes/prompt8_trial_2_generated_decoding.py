# Read a line of input from the user
input_string = input().rstrip()

# Calculate the length of the input string
string_length = len(input_string)

# Initialize a variable to keep track of the maximum length of repeating substrings
longest_repeating_length = 0

# Loop through possible lengths of substrings from 1 to string_length
for length in range(1, string_length + 1):
    
    # Nested loop to check each starting index in the string
    for starting_index in range(string_length - length + 1):
        
        # Extract the substring starting from starting_index with the current length
        current_substring = input_string[starting_index:starting_index + length]
        
        # Check if this substring appears again in the string after the current starting index
        if current_substring in input_string[starting_index + length:]:
            
            # If found, update longest_repeating_length to the current length
            longest_repeating_length = length

# Output the length of the longest repeating substring found
print(longest_repeating_length)


def longest_repeating_substring_length(input_string):
    input_string = input_string.rstrip()
    string_length = len(input_string)
    longest_repeating_length = 0

    for length in range(1, string_length + 1):
        for starting_index in range(string_length - length + 1):
            current_substring = input_string[starting_index:starting_index + length]
            if current_substring in input_string[starting_index + length:]:
                longest_repeating_length = length

    return longest_repeating_length

# Read input and call the function to print result
input_string = input()
print(longest_repeating_substring_length(input_string))
