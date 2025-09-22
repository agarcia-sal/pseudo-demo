def find_longest_repeated_substring():
    # Step 2: Read input from the user
    line = input().strip()
    line_length = len(line)
    
    # Step 3: Initialize a variable to keep track of the longest repeated substring length
    longest_repeated_substring_length = 0

    # Step 4: Iterate over possible substring lengths
    for current_length in range(1, line_length):  # Start at 1, since length 0 doesn't count as a substring
        # Step 4.1: Inner loop to check each starting index
        for start_index in range(line_length - current_length + 1):
            # Extract the current substring
            current_substring = line[start_index:start_index + current_length]

            # Check if the current substring appears later in the string
            if current_substring in line[start_index + current_length:]:
                # Update the longest repeated substring length if found
                longest_repeated_substring_length = current_length
                break  # No need to check further substrings of this length

    # Step 5: Output the result
    print(longest_repeated_substring_length)

# Call the function to execute
find_longest_repeated_substring()
