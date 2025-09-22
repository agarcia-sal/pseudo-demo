# Function to compare two strings and determine character frequency differences
def compare_strings():
    # Input: Accept two strings from the user
    string_one = input()
    string_two = input()

    # Process the Strings: Exclude spaces
    filtered_string_one = [char for char in string_one if char != ' ']
    filtered_string_two = [char for char in string_two if char != ' ']

    # Initialize frequencyDifference list
    frequency_difference = [0] * (ord('z') - ord('A') + 1)  # ASCII range from 'A' to 'z'

    # Count character frequencies
    for ascii_value in range(ord('A'), ord('z') + 1):
        char = chr(ascii_value)
        # Count occurrences in filtered strings
        count_in_string_one = filtered_string_one.count(char)
        count_in_string_two = filtered_string_two.count(char)
        
        # Calculate the difference and store it
        frequency_difference[ascii_value - ord('A')] = count_in_string_one - count_in_string_two

    # Check frequency conditions
    negative_counts = [diff for diff in frequency_difference if diff < 0]

    # Output the result based on the presence of negative counts
    if not negative_counts:  # if negative_counts is empty
        print("YES")
    else:
        print("NO")

# Note: The function can be tested by calling compare_strings() and entering inputs manually.
