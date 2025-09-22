def find_longest_repeating_substring():
    # Step 1: Initialize Program
    input_line = input().strip()  # Read input and remove trailing newline character
    length = len(input_line)       # Store length of the input line
    result = 0                     # Initialize result variable to 0

    # Step 2: Main Loop
    for sub_length in range(length):  # Iterate through substring lengths
        for start_index in range(length):  # Iterate through starting positions
            # Extract substring from input_line
            substring = input_line[start_index:start_index + sub_length + 1]  
            # Check if this substring appears again in input_line from the next position
            if (start_index + sub_length + 1 < length) and (substring in input_line[start_index + sub_length + 1:]):
                result = sub_length + 1  # Update the result to current length of substring
                break  # Break inner loop to test the next substring length

    # Step 3: Output the Result
    print(result)  # Print the length of the longest repeating substring

# Call the function to execute the program
find_longest_repeating_substring()
