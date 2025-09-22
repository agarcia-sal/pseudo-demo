def find_longest_repeated_substring(input_string):
    # Remove the last character from the input string
    processed_string = input_string[:-1]
    
    # Get the length of the processed string
    string_length = len(processed_string)
    
    # Initialize the variable to hold the length of the longest repeated substring
    longest_repeated_length = 0

    # Loop through possible substring lengths from 0 to string_length
    for substring_length in range(1, string_length + 1):  # Start from 1 to avoid empty substring
        # Loop through the starting index of substrings in processed_string
        for start_index in range(string_length - substring_length + 1):
            # Extract the substring from the processed_string
            current_substring = processed_string[start_index:start_index + substring_length]
            
            # Check if the current substring appears again in the processed_string
            if current_substring in processed_string[start_index + 1:]:
                # Update longest_repeated_length if a repeated substring is found
                longest_repeated_length = substring_length
                break  # Break out of inner loop since we found a repeated substring

    # Return the length of the longest repeated substring
    return longest_repeated_length

# Expected Usage
if __name__ == "__main__":
    input_string = input()  # Read input from standard input
    # Call the function and print the result
    print(find_longest_repeated_substring(input_string))
