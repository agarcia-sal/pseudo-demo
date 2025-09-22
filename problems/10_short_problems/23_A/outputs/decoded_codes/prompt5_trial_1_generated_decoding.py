# Function to find the length of the longest duplicate substring in a given string
def longest_duplicate_substring():
    # Read the input string from the user
    input_string = input().strip()

    # Determine the length of the input string
    string_length = len(input_string)

    # Initialize a variable to hold the maximum length of substring found
    longest_duplicate_length = 0

    # Loop through each possible length for substrings
    for substring_length in range(1, string_length):  # Start from 1 to avoid empty substring
        # Loop through each starting position in the string
        for start_position in range(string_length - substring_length + 1):  # Ensure substring fits
        
            # Extract a substring from the input string starting at start_position 
            # and having a length equal to substring_length
            current_substring = input_string[start_position:start_position + substring_length]

            # Check if this substring appears again in the input_string, starting just after its first occurrence
            if input_string.find(current_substring, start_position + 1) != -1:
                # If found, update the longest duplicate length
                longest_duplicate_length = substring_length
                break  # Exit inner loop, since we found a duplicate for this length

    # Output the length of the longest duplicate substring found
    print(longest_duplicate_length)

# Call the function to execute it
longest_duplicate_substring()
