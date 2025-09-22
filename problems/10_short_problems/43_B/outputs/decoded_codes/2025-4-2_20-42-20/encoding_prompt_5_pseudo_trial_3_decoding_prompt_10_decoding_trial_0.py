def compare_character_frequencies():
    # Get input strings from the user
    first_string = input()
    second_string = input()

    # Clean the input strings by removing spaces
    cleaned_strings = [first_string.replace(" ", ""), second_string.replace(" ", "")]

    # Initialize a list to store frequency differences
    frequency_differences = []

    # Check character counts for characters from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        char = chr(char_code)
        # Count occurrences of the current character in both cleaned strings
        count_first = cleaned_strings[0].count(char)
        count_second = cleaned_strings[1].count(char)

        # Calculate the difference in counts and store it
        frequency_difference = count_first - count_second
        frequency_differences.append(frequency_difference)

    # Check if all frequency differences are greater than or equal to zero
    if all(count >= 0 for count in frequency_differences):
        print("YES")  # Character frequencies match
    else:
        print("NO")   # Character frequencies do not match

# Execute the function
compare_character_frequencies()
