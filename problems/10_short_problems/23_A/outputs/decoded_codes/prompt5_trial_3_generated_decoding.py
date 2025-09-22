# Function to find the length of the longest substring that appears more than once
def longest_repeating_substring_length():
    # Read a line of input (string) and remove the last character (if any)
    input_line = input().rstrip('\n')
    
    # Calculate the length of the input string
    string_length = len(input_line)

    # Initialize the variable to store the length of the longest repeating substring
    longest_repeating_length = 0

    # Loop through all possible lengths of substrings from 1 to string_length
    for length in range(1, string_length):
        # Loop through each starting position for the substring
        for position in range(string_length - length):
            # Extract a substring of the current length starting from the current position
            current_substring = input_line[position:position + length]

            # Check if the substring appears again in the string after the current position
            if current_substring in input_line[position + 1:]:
                # If found, update the longest_repeating_length with the current length
                longest_repeating_length = length

                # Exit the inner loop as we've found a repeating substring of the current length
                break

    # Output the length of the longest repeating substring
    print(longest_repeating_length)

# Example test case (can be removed in production)
# longest_repeating_substring_length()  # Uncomment to test

