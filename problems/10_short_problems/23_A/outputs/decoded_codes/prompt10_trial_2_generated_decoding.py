def find_longest_repeating_substring():
    import sys

    # Read a line of input from standard input
    line = sys.stdin.readline().strip()
    
    n = len(line)  # Length of the line
    result_length = 0  # This variable stores the result

    # Iterate over possible substring lengths
    for length in range(1, n):  # Length starts from 1 up to n - 1
        # Check all starting points for the substring
        for start_index in range(n):
            substring = line[start_index:start_index + length]  # Get the substring

            # Check if the substring exists in the line starting from the next index
            if line.find(substring, start_index + 1) != -1:  # If found
                result_length = length  # Update the result length
                break  # Exit the inner loop as we found a repeating substring

    # Print the length of the longest repeating substring
    print(result_length)

# Call the function to execute
find_longest_repeating_substring()
