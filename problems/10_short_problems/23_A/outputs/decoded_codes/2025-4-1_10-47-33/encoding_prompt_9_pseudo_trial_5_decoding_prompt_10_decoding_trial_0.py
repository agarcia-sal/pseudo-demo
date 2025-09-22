def find_longest_repeated_substring():
    # Step 1: Get the Input
    input_string = input().strip()  # Read input and remove any trailing newline
    string_length = len(input_string)  # Store length of input string
    longest_repeated_substring_length = 0  # Initialize the length of the longest repeated substring

    # Step 2: Iterate Over Possible Substring Lengths
    for current_length in range(1, string_length):  # Start from length 1 to string_length - 1
        for start_position in range(string_length - current_length):  # Ensure not to exceed string bounds
            substring = input_string[start_position:start_position + current_length]  # Extract substring

            # Check if this substring appears again in the remainder of the string
            if substring in input_string[start_position + 1:]:
                longest_repeated_substring_length = current_length  # Update if found
                break  # Exit inner loop since we found a repeated substring

    # Step 3: Output the Length
    print(longest_repeated_substring_length)  # Print the final result

# Run the function
find_longest_repeated_substring()
