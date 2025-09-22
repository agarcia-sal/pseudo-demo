def find_longest_repeated_substring_length():
    # Read input string from the standard input
    input_string = input()
    
    # Determine the length of the input string
    length_of_string = len(input_string)
    
    # Initialize a variable to hold the length of the longest repeated substring
    longest_repeated_substring_length = 0

    # Loop through potential substring lengths from 1 to the full length of the string
    for substring_length in range(1, length_of_string):
        # Initialize an index for checking starting positions of substrings
        index = 0
        
        # Function to check for repeated substrings of a certain length
        def find_longest_substring(substring_length, index):
            nonlocal longest_repeated_substring_length  # Modify outer variable
            while index < length_of_string - substring_length + 1:
                # Extract a substring of the current length
                current_substring = input_string[index:index + substring_length]
                
                # Check if the substring appears again in the string after the current index
                if current_substring in input_string[index + 1:]:
                    # If found, it is a repeated substring, update the length
                    longest_repeated_substring_length = substring_length
                    return True
                
                # Move to the next starting position
                index += 1
            
            return False

        # Call the function to check for substrings of the current length
        found_repeated = find_longest_substring(substring_length, index)

        # If any repeated substring was found for this length, no need to check longer
        if found_repeated:
            break

    # Output the length of the longest repeated substring
    print(longest_repeated_substring_length)

# You can call the function to test
# find_longest_repeated_substring_length()  # Uncomment to run the function
