def find_longest_repeating_substring():
    # Step 1: Read a line of input and remove the last character (newline)
    input_line = input().strip()
    
    # Step 2: Store the length of the input line
    total_length = len(input_line)
    
    # Step 3: Initialize variable to track the longest repeating substring length
    longest_repeat_length = 0

    # Step 4: Loop through possible substring lengths from 0 to total_length
    for length in range(1, total_length + 1):
        # Step 4a: Loop through each starting index from 0 to total_length - length
        for start in range(total_length - length + 1):
            # Step 4ai: Extract the substring
            substring = input_line[start:start + length]
            # Step 4aii: Check if this substring appears again in the input
            if substring in input_line[start + 1:]:
                # Step 4aiii: If found, update the longest repeating length
                longest_repeat_length = length
                # Step 4aiv: Break out of the inner loop as we found a repeating substring
                break
                
    # Step 5: Print the longest found repeating substring length
    print(longest_repeat_length)

# Example usage:
find_longest_repeating_substring()
