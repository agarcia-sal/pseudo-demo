# Function to find the length of the longest repeated substring in a user input string.
def find_longest_repeated_substring_length():
    # Read a line of input and remove the trailing newline character
    user_input = input().strip()

    # Determine the length of the input line
    input_length = len(user_input)
    largest_verified_length = 0

    # Loop through possible substring lengths from 0 to input_length - 1
    for substring_length in range(input_length):
        # For each starting index in the user_input
        for start_index in range(input_length):
            # Extract the current substring of the specified length
            current_substring = user_input[start_index:start_index + substring_length]

            # Check if this substring appears again in the userInput after the startIndex 
            if current_substring in user_input[start_index + 1:]:
                # Update the largest verified length with the current substring length
                largest_verified_length = substring_length
                # Exit the inner loop as we found a repeat
                break
    
    # Output the largest length of the found repeated substring
    print(largest_verified_length)

# Call the function to execute
find_longest_repeated_substring_length()
