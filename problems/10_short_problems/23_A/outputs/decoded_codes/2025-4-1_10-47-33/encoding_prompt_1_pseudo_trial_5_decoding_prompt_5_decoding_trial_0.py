# Function to find the maximum length of repeated substring
def find_maximum_length_of_repeated_substring():
    # Read input line and strip trailing newline characters
    line = input().strip()
    length_of_line = len(line)

    # Initialize variable to track the maximum repeated length
    max_repeated_length = 0

    # Outer loop for each possible substring length
    for current_length in range(1, length_of_line):  # start from 1 to avoid empty substrings
        # Inner loop for starting index of the substring
        for start_index in range(length_of_line - current_length):
            # Extract the substring
            substring = line[start_index:start_index + current_length]
            # Check if the substring appears again in the line
            if substring in line[start_index + current_length:]:
                # Update max repeated length
                max_repeated_length = current_length
                break  # Found a repeat, no need to check further for this length

    # Output the result: length of the longest repeated substring
    print(max_repeated_length)

# Call the function to execute
find_maximum_length_of_repeated_substring()
