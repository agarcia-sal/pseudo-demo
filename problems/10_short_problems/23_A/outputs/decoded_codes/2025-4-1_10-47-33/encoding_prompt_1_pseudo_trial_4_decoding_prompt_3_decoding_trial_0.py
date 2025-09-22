def find_longest_repeating_substring():
    # Step 1: Initialize Program
    input_line = input().rstrip()  # Read input and remove trailing newline
    length = len(input_line)        # Store the length of input line
    result = 0                      # Initialize the result variable to 0

    # Step 2: Main Loop
    for sub_length in range(1, length):  # Start from 1 since substrings of length 0 are trivial
        for start_index in range(length - sub_length):  # Valid starting positions
            # Extract substring
            substring = input_line[start_index:start_index + sub_length]
            # Check if substring appears again in the input line
            if substring in input_line[start_index + 1:]:
                result = sub_length  # Update result with current substring length
                break  # Break out to test the next substring length

    # Step 3: Output the Result
    print(result)

# Function call to execute the program
find_longest_repeating_substring()
