def find_longest_repeating_substring():
    # Read input string from user
    input_string = input()
    string_length = len(input_string)
    
    # Variable to store the length of the longest repeating substring
    longest_repeating_substring_length = 0

    # Iterate through all possible substring lengths
    for current_length in range(1, string_length):
        # Check each starting position
        for start_index in range(string_length - current_length):
            # Extract the substring
            substring = input_string[start_index:start_index + current_length]
            
            # Search for the substring in the remaining part of the string
            if substring in input_string[start_index + current_length:]:
                longest_repeating_substring_length = current_length
                break  # No need to check further for this length

    # Output the length of the longest repeating substring found
    print(longest_repeating_substring_length)

# Run the function
find_longest_repeating_substring()
