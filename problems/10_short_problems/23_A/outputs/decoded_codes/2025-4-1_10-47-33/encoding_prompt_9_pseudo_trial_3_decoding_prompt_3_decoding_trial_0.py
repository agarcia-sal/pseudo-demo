def find_length_of_longest_repeated_substring():
    # Step 2: Receive Input
    input_string = input().rstrip('\n')  # Read a line and remove the newline character
    length_of_string = len(input_string)  # Store the length of the string
    longest_repeated_substring_length = 0  # Initialize to zero

    # Step 3: Loop Through Substring Lengths
    for current_length in range(length_of_string):  # Loop from 0 to length_of_string - 1
        for start_index in range(length_of_string - current_length):  # Define valid start index range
            # Extract substring from start index of current_length
            substring = input_string[start_index:start_index + current_length]

            # Check if the substring occurs again from index after start_index
            if substring in input_string[start_index + current_length:]:
                longest_repeated_substring_length = current_length  # Update the length if found
                break  # Break the inner loop as we found a match for this length

    # Step 4: Output Result
    print(longest_repeated_substring_length)

# Call the function to execute the program
find_length_of_longest_repeated_substring()
