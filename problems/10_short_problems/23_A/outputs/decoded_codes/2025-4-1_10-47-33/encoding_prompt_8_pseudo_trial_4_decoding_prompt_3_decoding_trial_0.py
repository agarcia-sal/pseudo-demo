def find_longest_repeated_substring():
    # Step 1: Read input
    input_line = input().strip()  # Read input line and remove any trailing newlines or spaces

    # Step 2: Initialize variables
    length_of_input = len(input_line)
    max_length = 0  # To track the length of the longest repeated substring

    # Step 3: Check for repeated substrings
    for current_length in range(1, length_of_input):  # Start from length 1 to length_of_input - 1
        for start_index in range(length_of_input - current_length + 1):
            # Step 5: Extract substring
            substring = input_line[start_index:start_index + current_length]

            # Step 6: Check if the substring appears again after its position
            if input_line.find(substring, start_index + 1) != -1:
                max_length = current_length  # Update max_length
                break  # No need to check further for this current_length

    # Step 7: Output the result
    print(max_length)

# Call the function to execute
find_longest_repeated_substring()
