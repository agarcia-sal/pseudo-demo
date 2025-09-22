def find_longest_repeating_substring():
    # Step 1: Receive Input
    input_line = input().strip()  # Read a line of input and remove trailing newline
    
    # Step 2: Initialize Variables
    length_of_line = len(input_line)  # Determine the length of the input line
    result_value = 0  # This will hold the length of the longest repeating substring
    
    # Step 3: Loop through Possible Substring Lengths
    for current_length in range(1, length_of_line):  # Start at 1 since length 0 won't have substrings
        for current_index in range(length_of_line - current_length):  # No need to start too close to the end
            # Get the substring of the current length
            substring = input_line[current_index:current_index + current_length]
            
            # Step 4: Check for Substring Reoccurrence
            if substring in input_line[current_index + 1:]:  # Check in the remaining string
                result_value = current_length  # Update the result value
                break  # Exit the inner loop since we've found a repeating substring
            
        # If we found a repeating substring of this length, no need to check longer lengths
        if result_value == current_length:
            break

    # Step 5: Output the Result
    print(result_value)

# Call the function to execute
find_longest_repeating_substring()
