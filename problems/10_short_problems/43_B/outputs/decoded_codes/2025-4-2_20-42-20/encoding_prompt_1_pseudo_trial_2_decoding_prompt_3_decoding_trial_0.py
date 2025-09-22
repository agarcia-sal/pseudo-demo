def can_form_from_strings():
    # Input: Read two lines of input strings
    first_string = input()
    second_string = input()
    
    # Process the Strings: Create filtered lists without spaces
    filtered_first = [char for char in first_string if char != ' ']
    filtered_second = [char for char in second_string if char != ' ']
    
    # Initialize Frequency Differences
    frequency_differences = []
    
    # Iterate through ASCII range from 'A' (65) to 'z' (122)
    for ascii_code in range(ord('A'), ord('z') + 1):
        char = chr(ascii_code)
        count_first = filtered_first.count(char)
        count_second = filtered_second.count(char)
        
        # Calculate the difference and append to frequency differences
        frequency_differences.append(count_first - count_second)
    
    # Check for Negative Frequencies
    negative_frequencies = [diff for diff in frequency_differences if diff < 0]
    
    # Output Result
    if len(negative_frequencies) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the code
can_form_from_strings()
