def longest_repeated_substring():
    # Step 2: Receive Input
    line = input().rstrip()  # Read a line of text and remove the trailing newline character
    line_length = len(line)  # Store the length of the line

    # Step 3: Initialize Counter
    longest_repeated_substring_length = 0

    # Step 4: Iterate Over Possible Substring Lengths
    for current_length in range(1, line_length):  # Start from length 1 to line_length - 1
        found = False  # To check if we found any repeated substring of this length

        for start_index in range(line_length - current_length + 1):  # Adjust range for substring extraction
            substring = line[start_index:start_index + current_length]  # Extract the substring

            # Check if this substring appears later in the line
            if substring in line[start_index + 1:]:  # Search only in the part after the current start_index
                longest_repeated_substring_length = current_length  # Update the maximum length found
                found = True  # Mark as found
                break  # Break out of the inner loop as we found a repeated substring

        if found:
            continue  # If a repeated substring has been found, continue to the next length

    # Step 5: Output the Result
    print(longest_repeated_substring_length)

# Ensure the function is called
longest_repeated_substring()
