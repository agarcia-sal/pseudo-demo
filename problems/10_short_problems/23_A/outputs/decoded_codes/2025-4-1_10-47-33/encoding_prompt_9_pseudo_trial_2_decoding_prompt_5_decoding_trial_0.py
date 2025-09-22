# Function to find the length of the longest repeating substring
def longest_repeating_substring_length():
    # Read input string from the user
    input_string = input()
    
    # Store the length of the input string
    string_length = len(input_string)
    
    # Initialize the length of the longest repeating substring to zero
    longest_repeating_length = 0
    
    # Iterate through possible substring lengths from 1 to string_length
    for current_length in range(1, string_length):
        # Iterate through starting positions of the substring
        for start_index in range(string_length - current_length):
            # Extract the substring of specified length
            substring = input_string[start_index:start_index + current_length]
            
            # Check for the existence of the substring in the rest of the string
            if substring in input_string[start_index + current_length:]:
                # Update the longest repeating substring length
                longest_repeating_length = max(longest_repeating_length, current_length)
                # No need to check other starting indices for this length
                break
    
    # Output the length of the longest repeating substring found
    print(longest_repeating_length)

# Test the function (uncomment to test)
# longest_repeating_substring_length()
