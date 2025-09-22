def find_longest_repeated_substring():
    # Step 1: Read input
    line = input().rstrip()  # Remove trailing newline from line
    total_length = len(line)  # Store the length of the line
    longest_repeated_length = 0  # Initialize to zero to track longest repeat

    # Step 2: Check substrings of each length
    for current_length in range(total_length):
        for start_index in range(total_length):
            # Step 2.1: Extracting the substring
            substring = line[start_index:start_index + current_length]

            # Step 2.2: Searching for the substring in the remainder of the line
            if substring in line[start_index + 1:]:  # Check in the remainder of the line
                # A repeated substring is found
                longest_repeated_length = current_length
                break  # Move on to the next length

    # Step 3: Output the longest found length
    print(longest_repeated_length)
