def compare_strings():
    # Read User Input
    first_string = input().replace(" ", "")  # Remove spaces from first string
    second_string = input().replace(" ", "")  # Remove spaces from second string

    # Initialize Frequency List
    frequency_differences = []

    # For each character from 'A' to 'z'
    for char in range(ord('A'), ord('z') + 1):
        char_in_first = first_string.count(chr(char))  # Count in first string
        char_in_second = second_string.count(chr(char))  # Count in second string
        
        # Calculate Difference
        difference = char_in_first - char_in_second
        frequency_differences.append(difference)  # Add Difference to frequencyDifferences

    # Check for Non-Negative Counts
    negative_count = sum(1 for diff in frequency_differences if diff < 0)  # Count negative differences

    # Output Result
    if negative_count == 0:  # If no negative counts in frequencyDifferences
        print("YES")
    else:
        print("NO")

# Call the function
compare_strings()
