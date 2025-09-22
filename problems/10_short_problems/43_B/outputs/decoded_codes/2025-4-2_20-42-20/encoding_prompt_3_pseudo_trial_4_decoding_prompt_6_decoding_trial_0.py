# Function to check frequency differences between two strings
def check_strings_difference():
    # Input: Two strings from the user
    first_string = input()  # Read the first string
    second_string = input()  # Read the second string

    # Process: Remove spaces from both strings
    cleaned_first_string = [char for char in first_string if char != ' ']
    cleaned_second_string = [char for char in second_string if char != ' ']

    # Initialize frequency difference list
    frequency_difference = []

    # Calculate frequency difference for each character in the ASCII range from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        first_string_count = cleaned_first_string.count(chr(character_code))
        second_string_count = cleaned_second_string.count(chr(character_code))
        difference = first_string_count - second_string_count

        # Append the difference to the frequency difference list
        frequency_difference.append(difference)

    # Determine if any frequency difference is negative
    negative_count = sum(1 for diff in frequency_difference if diff < 0)

    # Output: Print "YES" if all frequency differences are non-negative, otherwise print "NO"
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
check_strings_difference()
