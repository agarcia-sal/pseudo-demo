# Function to find the length of the longest repeating substring
def longest_repeating_substring():
    # Step 1: Read Input
    input_string = input()  # Obtain the string of characters
    string_length = len(input_string)  # Store the length of the string
    longest_repeating_substring_length = 0  # Initialize longest length variable

    # Step 2: Iterate Through Substring Lengths
    for current_length in range(1, string_length):  # Start from length 1 to string_length - 1
        # Inner loop to check every starting index for the current length
        for start_index in range(string_length - current_length + 1):  # Ensure valid index range
            # Step 1.1: Extract Substring
            substring = input_string[start_index:start_index + current_length]  # Get the substring

            # Step 1.2: Search for Repeats
            # Check if the substring appears in the remaining part of the string
            if input_string.find(substring, start_index + 1) != -1:  # Look for the substring beyond current start
                # Update longest length found
                longest_repeating_substring_length = current_length
                break  # No need to check other starting indices for this length

    # Step 3: Output Result
    print(longest_repeating_substring_length)  # Print the maximum length found

# Call the function to execute the functionality
longest_repeating_substring()
