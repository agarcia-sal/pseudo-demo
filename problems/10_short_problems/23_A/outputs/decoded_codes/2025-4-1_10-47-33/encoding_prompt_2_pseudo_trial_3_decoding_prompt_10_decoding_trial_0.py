def longest_repeating_substring():
    # Step 1: Input
    text_line = input().strip()  # Read input and strip newline characters
    
    # Step 2: Initialize variables
    text_length = len(text_line)  # Get the length of the input line
    maximum_length = 0  # Variable to keep track of the longest repeating substring length

    # Step 3: Outer Loop to iterate through different substring lengths
    for current_length in range(1, text_length):  # Start from 1 to text_length - 1
        # Step 3: Inner Loop for starting positions of substrings
        for start_position in range(text_length - current_length):  # Valid starting positions
            substring = text_line[start_position:start_position + current_length]  # Extract substring
            # Check if the substring appears again in the rest of the string
            if substring in text_line[start_position + current_length:]:
                maximum_length = current_length  # Update maximum length if found
                break  # Exit the inner loop for the current substring length

    # Step 4: Output the maximum length found
    print(maximum_length)

# Example execution
longest_repeating_substring()
