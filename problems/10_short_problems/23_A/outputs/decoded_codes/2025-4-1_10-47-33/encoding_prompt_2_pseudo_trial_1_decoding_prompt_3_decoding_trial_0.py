def find_longest_repeated_substring():
    # Step 1: Read input
    user_input = input().strip()
    
    # Step 2: Determine length
    string_length = len(user_input)
    
    # Step 3: Initialize variable
    repeated_substring_length = 0

    # Step 4: Outer loop for each possible substring length
    for substring_length in range(1, string_length):
        # Step 4.1: Inner loop for each possible starting index
        for start_index in range(string_length - substring_length):
            # Extract substring
            substring = user_input[start_index:start_index + substring_length]

            # Check if this substring appears again in the string
            if substring in user_input[start_index + substring_length:]:
                # Update longest repeated substring length
                repeated_substring_length = substring_length
                break  # Exit inner loop when a repeat is found

    # Step 5: Output result
    print(repeated_substring_length)

# Example of usage
find_longest_repeated_substring()
