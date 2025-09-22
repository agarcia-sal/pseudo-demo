def longest_repeated_substring_length():
    # Step 1: Read Input
    input_line = input().rstrip('\n')  # Removing the trailing newline
    line_length = len(input_line)

    # Step 2: Initialize Variable
    max_length = 0

    # Step 3: Outer Loop for each possible substring length
    for current_length in range(1, line_length + 1):
        # Step 3.1: Inner Loop for the start index of the substring
        for current_index in range(line_length):
            # Step 3.1.1: Extract the substring
            substring = input_line[current_index:current_index + current_length]

            # Step 3.1.2: Check for repetition of the substring
            if substring in input_line[current_index + 1:]:
                # Step 3.1.3: Update max_length if repetition is found
                max_length = current_length
                break  # Exit inner loop, as we found a repetition
        
    # Step 4: Output Result
    print(max_length)

# To execute the function
longest_repeated_substring_length()
