def find_longest_repeated_substring_length():
    # Step 1: Read input from the user
    user_input = input().strip()
    
    # Step 2: Calculate the length of the input string
    string_length = len(user_input)
    
    # Step 3: Initialize the variable to track the length of the longest repeated substring
    repeated_substring_length = 0

    # Step 4: Outer loop for each possible substring length
    for substring_length in range(1, string_length):
        # Step 4.1: Inner loop for each starting index in the string
        for start_index in range(string_length - substring_length):
            # Step 4.2: Extract the current substring
            current_substring = user_input[start_index:start_index + substring_length]
            
            # Step 4.3: Check if this substring appears again in the string from the next index onward
            if user_input.find(current_substring, start_index + 1) != -1:
                # Step 4.4: Update repeated_substring_length and exit inner loop
                repeated_substring_length = substring_length
                break  # Exit the inner loop since we found a repeated substring

    # Step 5: Output the result
    print(repeated_substring_length)

# Example use case
find_longest_repeated_substring_length()
