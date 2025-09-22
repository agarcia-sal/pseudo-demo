def find_length_of_longest_repeating_substring():
    # Read a line of input from the user
    input_string = input()
    
    # Calculate the length of the input string
    string_length = len(input_string)
    
    # Initialize a variable to store the length of the longest repeating substring
    longest_repeating_length = 0

    # Iterate over all possible lengths of substrings
    for substring_length in range(string_length):
        # Check for each starting position in the string
        for start_index in range(string_length):
            # Extract the substring from current index of specified length
            current_substring = extract_substring(input_string, start_index, substring_length)

            # Check if this current substring exists later in the input_string
            if exists_in_string(input_string, current_substring, start_index + 1):
                # If it does exist, update longest_repeating_length
                longest_repeating_length = substring_length
                break  # Stop checking this length since we've already found a match

    # Output the length of the longest repeating substring found
    print(longest_repeating_length)

def extract_substring(string, start_index, length):
    # Return substring of string starting from start_index of specified length
    return string[start_index:start_index + length]

def exists_in_string(string, sub_string, start_index):
    # Check if sub_string appears in string starting from start_index
    return sub_string in string[start_index:]

# Call the function to execute
find_length_of_longest_repeating_substring()
