# Function to find the length of the longest substring that appears more than once in a given string
def longest_repeated_substring_length():
    # Read a line of text from the user
    input_string = input().rstrip()  # Remove the newline character at the end
    length_of_string = len(input_string)  # Store the length of the string
    longest_repeated_substring_length = 0  # Initialize variable to store the length of the longest repeated substring
    
    # Loop through each possible length of substrings
    for current_length in range(length_of_string):  # Loop from 0 to length_of_string - 1
        for start_index in range(length_of_string - current_length):  # Loop through each starting index
            # Extract the substring
            substring = input_string[start_index:start_index + current_length + 1]
            # Check if this substring occurs again in the string
            if input_string.find(substring, start_index + 1) != -1:  # Check for subsequent occurrence
                longest_repeated_substring_length = current_length + 1  # Update if found
                break  # Only need the first occurrence for the longest length
    
    # Output the result
    print(longest_repeated_substring_length)

# Example of how the function might be executed
# longest_repeated_substring_length() 

# You can test the function by providing different inputs when prompted.
