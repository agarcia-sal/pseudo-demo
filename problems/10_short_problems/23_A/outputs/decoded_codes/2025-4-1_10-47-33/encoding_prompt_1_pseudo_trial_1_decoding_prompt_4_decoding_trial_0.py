def find_longest_repeated_substring_length():
    # Step 1: Read input and remove any trailing newline character
    input_line = input().strip()
    
    # Step 2: Determine the length of the input line
    length_of_input = len(input_line)
    
    # Step 3: Initialize the variable for longest repeated substring length
    longest_repeated_substring_length = 0

    # Step 4: Iterate over all possible lengths of substrings
    for current_length in range(length_of_input):
        # Step 4a: Iterate over all starting positions for the current length
        for start_index in range(length_of_input):
            # Step 4ai: Extract the substring of the current length
            current_substring = input_line[start_index:start_index + current_length]
            
            # Step 4aii: Check if this substring appears again in the input line
            if (current_substring and 
                input_line.find(current_substring, start_index + 1) != -1):
                # Step 4aiii: Update the longest repeated substring length
                longest_repeated_substring_length = current_length + 1
                
                # Exit the inner loop to check the next current_length
                break
                
    # Step 5: Print the result
    print(longest_repeated_substring_length)

# Call the function
find_longest_repeated_substring_length()
