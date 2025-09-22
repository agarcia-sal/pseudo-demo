# Function to find the length of the longest substring that appears more than once
def longest_repeated_substring_length():
    # Read input string and remove the last character
    input_string = input()[:-1]
    length_of_string = len(input_string)
    longest_repeated_length = 0  # Initialize the longest repeated length to 0

    # Loop through all possible substring lengths
    for substring_length in range(1, length_of_string):  # Start from 1 to length_of_string - 1
        # Check each starting index for the current substring length
        for index in range(length_of_string - substring_length + 1):  # Ensure we don't go out of bounds
            # Extract current substring
            current_substring = input_string[index:index + substring_length]

            # Check if current_substring appears again in input_string
            if current_substring in input_string[index + 1:]:
                longest_repeated_length = substring_length  # Update longest repeated length
                break  # Exit the inner loop as we found a repeated substring

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Example test cases (these are just comments for testing purposes)
# To test the function, you can uncomment the following line and run the code to see results:
# longest_repeated_substring_length()
