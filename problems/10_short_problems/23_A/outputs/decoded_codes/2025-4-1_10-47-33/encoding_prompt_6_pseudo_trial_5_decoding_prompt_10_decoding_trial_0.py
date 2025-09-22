def find_longest_repeating_substring_length():
    # Step 1: Read input
    input_string = input().rstrip()  # Removing the newline character
    total_length = len(input_string)  # Step 2: Get the length of the input string
    longest_repeat_length = 0  # Step 3: Initialize the longest repeating substring length

    # Step 4: Loop through possible substring lengths
    for length in range(total_length + 1):
        # Step 4a: Loop through each starting index
        for start_index in range(total_length):
            # Step 4ai: Extract substring from current index with the current length
            substring = input_string[start_index:start_index + length]
            # Step 4aii: Check if this substring appears again after the current index
            if (substring in input_string[start_index + length:]):
                # Step 4aiii: If found, update the longest repeating length
                longest_repeat_length = length
                break  # Step 4aiv: Break out of the inner loop if a repeating substring is found

    # Step 5: Output the longest repeating substring length
    print(longest_repeat_length)

# Function execution
find_longest_repeating_substring_length()
