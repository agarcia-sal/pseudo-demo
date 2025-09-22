def find_longest_repeated_substring(input_string):
    # Initialize the length of the input string
    string_length = len(input_string)
    # Initialize the variable to store the length of the longest repeated substring
    longest_repeated_length = 0
    
    # Loop over each possible length of substring, starting from 0 to string_length - 1
    for current_length in range(1, string_length):  # Start from 1 to avoid empty substrings
        # Loop over each starting position of the substring
        for starting_index in range(string_length - current_length + 1):  # Ensure we don't go out of bounds
            # Extract the substring we are checking
            substring = input_string[starting_index:starting_index + current_length]
            # Check if the substring exists again in the string after the current starting index
            if substring in input_string[starting_index + 1:]:
                # Update longest_repeated_length to current_length, indicating a repeated substring was found
                longest_repeated_length = current_length
                # Exit the inner loop once a repeated substring is found at this length
                break  # Break out of the inner loop
    
    # Return the length of the longest repeated substring found
    return longest_repeated_length

# Read input string from the user
input_string = input()
# Call the function and print the result
print(find_longest_repeated_substring(input_string))
