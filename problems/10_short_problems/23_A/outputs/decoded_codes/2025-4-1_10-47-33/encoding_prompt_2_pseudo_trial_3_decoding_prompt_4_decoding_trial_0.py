def find_longest_repeating_substring():
    # Step 1: Input - Read a line of text
    text_line = input().strip()  # Strip to remove trailing new line character
    
    # Step 2: Initialize
    text_length = len(text_line)  # Determine the length of the line of text
    maximum_length = 0  # Initialize maximumLength to zero

    # Step 3: Outer Loop
    for current_length in range(1, text_length):  # currentLength from 1 to textLength - 1
        # Step 3: Inner Loop
        for start_position in range(text_length - current_length + 1):  # Ensure the substring range is valid
            # Extract substring
            substring = text_line[start_position:start_position + current_length]
            # Check if this substring appears again in the text
            if substring in text_line[start_position + current_length:]:
                # Update maximumLength and break
                maximum_length = current_length
                break  # Exit inner loop since we found a valid repetition

    # Step 4: Output
    print(maximum_length)

# Call the function to execute
find_longest_repeating_substring()
