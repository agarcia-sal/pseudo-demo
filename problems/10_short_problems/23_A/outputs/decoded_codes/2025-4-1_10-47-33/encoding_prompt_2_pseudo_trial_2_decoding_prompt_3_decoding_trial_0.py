# Function to find the longest repeated substring in a given line of text
def find_longest_repeated_substring():
    # Step 1: Read Input
    line = input().rstrip()  # Obtain a line of text and remove trailing newline characters
    line_length = len(line)   # Determine the length of the input line

    # Step 2: Initialize Variable
    max_length = 0  # Max length of repeated substring found

    # Step 3: Outer Loop for each possible substring length
    for current_length in range(1, line_length):  # Start from 1 to avoid 0 length
        # Inner Loop for each character index within the range of line_length
        for current_index in range(line_length - current_length + 1):
            # Step 1: Extract Substring
            sub_string = line[current_index:current_index + current_length]
            
            # Step 2: Check for Repetition
            if line.find(sub_string, current_index + 1) != -1:  # Search after current_index
                max_length = current_length  # Update max_length
                break  # Exit the inner loop if a repeated substring is found

    # Step 4: Output Result
    print(max_length)  # Display the length of the longest repeated substring found

# Call the function
find_longest_repeated_substring()
