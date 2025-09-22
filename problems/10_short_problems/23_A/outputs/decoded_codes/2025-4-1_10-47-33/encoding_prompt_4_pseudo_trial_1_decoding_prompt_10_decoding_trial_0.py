def find_longest_repeating_length():
    # Read a line of input from the user
    input_line = input()
    
    # Get the length of the input line
    n = len(input_line)
    
    # Initialize return value
    longest_repeating_length = 0

    # Iterate over possible substring lengths
    for length in range(1, n):  # length starts from 1 to n-1
        # Check for each starting index in the string
        for start_index in range(n):
            # Extract the substring of the current length
            substring = input_line[start_index:start_index + length]
            
            # Check if this substring exists again in the string after the start_index
            if substring in input_line[start_index + 1:]:
                # Update longest repeating length if found
                longest_repeating_length = length
                break  # Exit inner loop if a repeat is found

    # Output the length of the longest repeating substring found
    print(longest_repeating_length)

# Ensure the function runs when the script is executed
if __name__ == "__main__":
    find_longest_repeating_length()
