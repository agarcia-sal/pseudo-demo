def compare_string_frequencies():
    # Input two strings and remove spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")
    
    # Initialize a list to hold frequency differences for characters from 'A' to 'z'
    frequency_differences = []
    
    # Loop through ASCII values from 'A' (65) to 'z' (122)
    for ascii_value in range(65, 123):
        # Count occurrences of the character in both strings
        count_first_string = first_string.count(chr(ascii_value))
        count_second_string = second_string.count(chr(ascii_value))
        
        # Calculate frequency difference and store it in the list
        frequency_difference = count_first_string - count_second_string
        frequency_differences.append(frequency_difference)
    
    # Count how many differences are negative
    negative_count = sum(1 for diff in frequency_differences if diff < 0)
    
    # Check if there are no negative differences
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Example test cases
# Uncomment to run tests
# compare_string_frequencies()  # Input: "abcdef" and "abc"
# compare_string_frequencies()  # Input: "hello" and "world"
