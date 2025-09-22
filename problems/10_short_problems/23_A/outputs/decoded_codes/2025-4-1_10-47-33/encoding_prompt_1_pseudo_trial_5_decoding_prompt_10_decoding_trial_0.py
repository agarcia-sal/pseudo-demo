def find_maximum_repeated_length():
    # Step 1: Read input
    line = input().rstrip()
    length_of_line = len(line)
    
    # Step 2: Initialize variables
    max_repeated_length = 0

    # Step 3: Outer Loop: Iterate through possible substring lengths
    for current_length in range(1, length_of_line):  # Start from length 1 to length_of_line - 1
        # Step 3: Inner Loop: Check each starting index for substrings
        for start_index in range(length_of_line - current_length + 1):
            # Extract the substring
            substring = line[start_index:start_index + current_length]
            # Check for repeated substring
            if substring in line[start_index + 1:]:
                # If found, update max_repeated_length
                max_repeated_length = current_length
                break  # Found a repeat, no need to check other start indices

    # Step 4: Output the result
    print(max_repeated_length)

# Testing the function
if __name__ == "__main__":
    find_maximum_repeated_length()
