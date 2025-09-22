def find_longest_repeated_substring():
    # Step 1: Read a line of input and remove the trailing newline character.
    input_line = input().strip()
    
    # Step 2: Determine the length of the input line.
    length_of_line = len(input_line)
    
    # Step 3: Initialize a variable to hold the length of the longest repeated substring.
    repeated_substring_length = 0

    # Step 4: Iterate through possible substring lengths.
    for substring_length in range(1, length_of_line):  # Start from 1 to avoid empty substring
        # Step 4.1: For each starting index in the line.
        for start_index in range(length_of_line - substring_length + 1):
            # Step 4.2: Extract the substring.
            substring = input_line[start_index:start_index + substring_length]
            
            # Step 4.3: Check if this substring appears later in the string.
            if substring in input_line[start_index + substring_length:]:
                # Step 4.4: Update longest repeated substring length.
                repeated_substring_length = substring_length
                break  # Exit the inner loop once a repeated substring is found.
        
        # If a repeated substring is found for the current length, exit the outer loop as well.
        if repeated_substring_length != 0:
            break

    # Step 5: Output the length of the longest repeated substring.
    print(repeated_substring_length)

# Run the function
find_longest_repeated_substring()
