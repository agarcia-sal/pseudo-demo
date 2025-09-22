def check_strings_difference():
    # Input: Read two strings from the user
    first_string = input()
    second_string = input()

    # Process: Remove spaces from both strings
    cleaned_first_string = [char for char in first_string if char != ' ']
    cleaned_second_string = [char for char in second_string if char != ' ']

    # Initialize frequency difference list
    frequency_difference = []

    # Calculate frequency difference for each character in the ASCII range from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        # Count occurrences of the character in both cleaned strings
        first_string_count = cleaned_first_string.count(chr(character_code))
        second_string_count = cleaned_second_string.count(chr(character_code))

        # Calculate the difference and append it to the frequency difference list
        difference = first_string_count - second_string_count
        frequency_difference.append(difference)

    # Determine if any frequency difference is negative
    negative_count = sum(1 for diff in frequency_difference if diff < 0)

    # Output: Print "YES" if all frequency differences are non-negative, otherwise print "NO"
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Test the function (uncomment to run tests)
# check_strings_difference()
