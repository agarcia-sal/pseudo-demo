def find_longest_repeated_substring(input_string):
    # Get the length of the input string
    length_of_string = len(input_string)
    longest_repeated_substring_length = 0

    # Iterate over possible substring lengths
    for substring_length in range(1, length_of_string):  # Starting from 1 to avoid empty substring
        for start_index in range(length_of_string):
            # Define the current substring
            current_substring = input_string[start_index:start_index + substring_length]
            # Check if the current substring appears again in the input string after the current start index
            if (input_string.find(current_substring, start_index + 1) != -1):
                # Update the longest length found
                longest_repeated_substring_length = substring_length
                break  # Exit inner loop when a repeat is found

    return longest_repeated_substring_length

# Driver code
input_string = input()  # Read input from standard input
print(find_longest_repeated_substring(input_string))
