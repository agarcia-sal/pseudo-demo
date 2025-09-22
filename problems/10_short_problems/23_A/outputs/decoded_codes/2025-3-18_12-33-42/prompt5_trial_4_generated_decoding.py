# Function to find the length of the longest prefix that repeats elsewhere in the string
def longest_repeating_prefix():
    # Read the input string
    string_line = input().strip()
    
    # Get the length of the string
    string_length = len(string_line)
    
    # Initialize the variable to keep track of the longest repeating prefix length
    longest_repeating_prefix_length = 0
    
    # Iterate over possible prefix lengths from 1 to string_length - 1
    for prefix_length in range(1, string_length):
        # Check for repeated substrings of the current prefix length
        for start_index in range(0, string_length - prefix_length):
            # Extract the substring from start_index with the current prefix length
            prefix_substring = string_line[start_index:start_index + prefix_length]
            
            # Search for the prefix_substring in the remainder of the string
            if prefix_substring in string_line[start_index + prefix_length:]:
                longest_repeating_prefix_length = prefix_length
                break  # Exit the inner loop if we found a repeating prefix
        
    # Output the length of the longest repeating prefix found
    print(longest_repeating_prefix_length)

# Example usage (commented out to avoid execution during import)
# longest_repeating_prefix()
