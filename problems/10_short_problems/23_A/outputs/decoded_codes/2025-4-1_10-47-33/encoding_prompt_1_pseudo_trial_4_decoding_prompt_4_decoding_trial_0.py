def find_longest_repeating_substring():
    # Step 1: Initialize Program
    input_line = input().strip()  # Read input and remove trailing newline
    length = len(input_line)       # Store the length of the input line
    result = 0                     # Initialize the result for longest repeating substring length

    # Step 2: Main Loop
    for sub_length in range(1, length):  # Iterate through possible substring lengths
        for start_index in range(length - sub_length):  # Iterate through starting indices
            substring = input_line[start_index:start_index + sub_length]  # Extract substring

            # Check if the substring appears again in the input_line
            if substring in input_line[start_index + 1:]:  # Search in the remaining part of the string
                result = sub_length  # Update result to current sub_length
                break  # Move to next substring length if found

    # Step 3: Output the Result
    print(result)

# Invoke the function to run the program
find_longest_repeating_substring()
