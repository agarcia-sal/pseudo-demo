# Function to find the length of the longest repeated substring in a given string
def longest_repeated_substring_length():
    # Read input from the user
    input_string = input().strip()
    
    # Determine the length of the input string
    length_of_input_string = len(input_string)
    
    # Initialize the variable to track the length of the longest repeated substring
    longest_repeated_substring_length = 0
    
    # Loop through each possible length of substrings
    for current_length in range(1, length_of_input_string):  # Substrings of length 1 to n-1
        # Check each starting position for the current length
        for start_position in range(length_of_input_string - current_length + 1):  # Valid starting positions
            # Extract the current substring
            current_substring = input_string[start_position:start_position + current_length]
            
            # Check if the substring can be found elsewhere in the string
            if current_substring in input_string[start_position + 1:]:  # Looking for repeat after the start position
                # Update the longest repeated substring length
                longest_repeated_substring_length = current_length
                break  # Break out of the inner loop once a repeat is found

    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# To test the function, you may uncomment the following line:
# longest_repeated_substring_length()
