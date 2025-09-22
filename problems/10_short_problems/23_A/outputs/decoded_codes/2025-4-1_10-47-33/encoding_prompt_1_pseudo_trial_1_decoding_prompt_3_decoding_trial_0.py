def find_longest_repeated_substring():
    # Step 1: Read a line of input and remove any trailing newline character.
    input_line = input().strip()
    
    # Step 2: Determine the length of the input line.
    length_of_input = len(input_line)
    
    # Step 3: Initialize variable for longest repeated substring's length.
    longest_repeated_substring_length = 0
    
    # Step 4: Iterate over each possible length of substring.
    for current_length in range(1, length_of_input):  # Length should start from 1
        # Step 4a: Check substrings of length 'current_length'.
        for start_index in range(length_of_input - current_length + 1):
            # Step 4b: Extract the substring from input_line.
            current_substring = input_line[start_index:start_index + current_length]
            
            # Step 4c: Check for occurrence of the substring after start_index.
            if input_line.find(current_substring, start_index + 1) != -1:
                # If we find the substring again, update the longest length.
                longest_repeated_substring_length = current_length  # Update to the current length
                break  # Exit inner loop once a repeated substring is found
    
    # Step 5: Print the result.
    print(longest_repeated_substring_length)

# Call the function to execute.
find_longest_repeated_substring()
