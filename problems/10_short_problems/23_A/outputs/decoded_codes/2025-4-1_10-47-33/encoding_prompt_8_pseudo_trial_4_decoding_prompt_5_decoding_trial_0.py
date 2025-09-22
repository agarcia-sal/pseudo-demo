# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Step 1: Read input
    input_line = input().strip()  # Read input and remove trailing newline

    # Step 2: Initialize variables
    length_of_input = len(input_line)  # Get the length of the input string
    max_length = 0  # To track the length of the longest repeated substring

    # Step 3: Check for repeated substrings
    for current_length in range(1, length_of_input):  # Start from 1 to avoid empty substrings
        for start_index in range(length_of_input - current_length):  # Ensure we do not go out of bounds
            # Step 5: Extract substring
            substring = input_line[start_index:start_index + current_length]

            # Step 6: Check if the substring appears again after its position
            if input_line.find(substring, start_index + 1) != -1:
                max_length = current_length  # Update maxLength
                break  # Exit inner loop as we found a repeat

    # Step 7: Output the result
    print(max_length)

# Uncomment below line to test the function
# longest_repeated_substring()
