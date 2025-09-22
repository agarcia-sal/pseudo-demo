def longest_repeated_substring():
    # Step 1: Read input and remove any trailing newline character
    input_line = input().strip()
    
    # Step 2: Determine input length
    length_of_input = len(input_line)
    
    # Step 3: Initialize the length of the longest repeated substring
    longest_repeated_substring_length = 0
    
    # Step 4: Loop through possible lengths of substrings
    for current_length in range(1, length_of_input):  # Start from 1 to avoid empty substring
        # Step 4a: Loop through each start index
        for start_index in range(length_of_input - current_length + 1):
            # Step 4b: Extract current substring
            current_substring = input_line[start_index:start_index + current_length]
            
            # Step 4c: Check if substring appears again in input line
            if current_substring in input_line[start_index + current_length:]:
                # Step 4d: Update the longest repeated substring length
                longest_repeated_substring_length = current_length
                # Exit the inner loop once a match is found
                break
                
    # Step 5: Print the result
    print(longest_repeated_substring_length)

# Function call to execute the function
longest_repeated_substring()
