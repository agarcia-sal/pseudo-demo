def find_maximum_length_of_repeated_substring():
    # Step 1: Read Input
    line = input().rstrip('\n')  # Read a line of text input and remove the trailing newline character
    length_of_line = len(line)  # Store the length of this line

    # Step 2: Initialize Variables
    max_repeated_length = 0  # Initialize the maximum repeated substring length to 0

    # Step 3: Outer Loop
    for current_length in range(1, length_of_line):  # Start from 1 up to length_of_line - 1
        # Step 3.1: Inner Loop
        for start_index in range(length_of_line - current_length + 1):  # Adjust range based on current_length
            # Extract substring
            substring = line[start_index:start_index + current_length]
            # Check if this substring appears again
            next_index = line.find(substring, start_index + 1)  # Find next occurrence
            
            if next_index != -1:  # Substring found again
                max_repeated_length = current_length  # Update max length
                break  # Stop inner loop since we found a repeat

    # Step 4: Output Result
    print(max_repeated_length)  # Print the maximum repeated length

# Example usage
find_maximum_length_of_repeated_substring()
