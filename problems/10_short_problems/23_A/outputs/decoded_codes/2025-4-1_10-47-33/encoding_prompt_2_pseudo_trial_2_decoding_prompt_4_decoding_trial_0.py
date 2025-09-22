def find_max_repeated_substring_length():
    # Step 1: Read input line
    input_line = input().rstrip('\n')
    line_length = len(input_line)

    # Step 2: Initialize variable for maximum repeated substring length
    max_length = 0

    # Step 3: Outer loop for substring length
    for current_length in range(line_length):
        # Step 3.1: Inner loop for character index
        for current_index in range(line_length):
            # Step 3.1.1: Extract substring
            sub_string = input_line[current_index:current_index + current_length]
            
            # Check if the substring is valid (avoid out of bounds)
            if len(sub_string) == current_length:
                # Step 3.1.2: Check for repetition
                # Start searching after the current index to find a repeat
                if input_line.find(sub_string, current_index + 1) != -1:
                    # Step 3.1.3: Update maximum length
                    max_length = current_length + 1  # Current length +1 because of zero-indexing
                    break  # Exit inner loop once a repeat is found

    # Step 4: Output result
    print(max_length)

# Call the function to execute the logic
find_max_repeated_substring_length()
