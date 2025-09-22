def longest_repeating_substring_length():
    # Step 1: Read a line of input and remove the last character (newline)
    input_string = input().rstrip('\n')
    
    # Step 2: Store the length of the input line in a variable called totalLength
    total_length = len(input_string)
    
    # Step 3: Initialize a variable longestRepeatLength to 0
    longest_repeat_length = 0
    
    # Step 4: Loop through possible substring lengths from 1 to totalLength
    for length in range(1, total_length + 1):
        # Step 4a: Loop through each starting index from 0 to totalLength - length
        for start_index in range(total_length - length + 1):
            # Step 4ai: Extract a substring starting from the current index with the current length
            substring = input_string[start_index:start_index + length]
            
            # Step 4aii: Check if this substring appears again in the input
            # Starting after the current index
            if substring in input_string[start_index + length:]:
                # Step 4aiii: If found, update longestRepeatLength
                longest_repeat_length = length
                # Step 4aiv: Break out of the inner loop
                break
    
    # Step 5: Print longestRepeatLength
    print(longest_repeat_length)

# Call the function to execute
longest_repeating_substring_length()
