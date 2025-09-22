def compare_strings():
    # Get input from the user, two separate strings
    first_input = input()
    second_input = input()

    # Remove spaces from both input strings
    first_string_characters = [char for char in first_input if char != ' ']
    second_string_characters = [char for char in second_input if char != ' ']

    # Initialize a dictionary to store frequency counts
    frequency_first = {}
    frequency_second = {}

    # Count occurrences of each character in first string
    for char in first_string_characters:
        if char in frequency_first:
            frequency_first[char] += 1
        else:
            frequency_first[char] = 1

    # Count occurrences of each character in second string
    for char in second_string_characters:
        if char in frequency_second:
            frequency_second[char] += 1
        else:
            frequency_second[char] = 1

    # Check if the first string has enough characters to match the second string
    for char in frequency_second:
        if frequency_first.get(char, 0) < frequency_second[char]:
            print("NO")
            return

    print("YES")

# Testing the function with various inputs
compare_strings()
