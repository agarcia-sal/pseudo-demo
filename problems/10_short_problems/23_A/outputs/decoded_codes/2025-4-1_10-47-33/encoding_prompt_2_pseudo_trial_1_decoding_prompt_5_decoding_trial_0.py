# Function to find the length of longest repeated substring in a given string
def longest_repeated_substring_length():
    # Step 1: Read input and remove trailing newline
    input_string = input().strip()
    
    # Step 2: Determine the length of the input string
    string_length = len(input_string)
    
    # Step 3: Initialize variable to track length of longest repeated substring
    repeated_substring_length = 0

    # Step 4: Outer loop to check all substring lengths
    for substring_length in range(1, string_length):  # Start from 1 to avoid empty substring
        # Inner loop for possible starting indices
        for start_index in range(string_length - substring_length):
            # Extract the current substring
            substring = input_string[start_index:start_index + substring_length]
            
            # Check if the substring appears again in the string
            if substring in input_string[start_index + substring_length:]:
                # Update the length of the repeated substring
                repeated_substring_length = substring_length
                break  # Exit inner loop as a repeat has been found

    # Step 5: Output result
    print(repeated_substring_length)

# Call the function to test
longest_repeated_substring_length()

# Test cases can be added as comments
# Input: "abcabc"
# Output: 3 (the substring "abc" is repeated)
# Input: "aaaa"
# Output: 1 (the substring "a" is repeated)
# Input: "" (empty string)
# Output: 0 (no substrings)
