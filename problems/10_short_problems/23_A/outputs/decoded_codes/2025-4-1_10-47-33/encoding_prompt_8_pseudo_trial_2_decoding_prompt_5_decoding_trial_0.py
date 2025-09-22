# Function to find the length of the longest repeated substring
def longest_repeated_substring_length():
    # Read input line of text
    input_line = input().strip()[:-1]  # Exclude the last character

    # Determine the length of the input line
    length_of_line = len(input_line)
    longest_repeated_length = 0  # Variable to store the length of the longest repeated substring

    # Outer loop: iterate through potential substring lengths
    for current_length in range(1, length_of_line):  # Starting from 1 to length_of_line - 1
        # Inner loop: iterate through possible starting positions
        for start_index in range(length_of_line - current_length + 1):
            # Extract substring of the current length
            substring = input_line[start_index:start_index + current_length]
            
            # Check for repetition of the substring in the remaining part of the input line
            if substring in input_line[start_index + current_length:]:
                longest_repeated_length = current_length  # Update longest repeated length
                break  # We found a repetition, exit inner loop

    # Output the result
    print(longest_repeated_length)

# You may invoke the function to test it with different inputs
# Uncomment the line below to run the function interactively
# longest_repeated_substring_length()
