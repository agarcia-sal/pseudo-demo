def check_letter_frequencies():
    """
    This function reads two strings from the user, removes spaces,
    and checks if the frequency of each character in the first string
    is greater than or equal to the frequency of the corresponding
    character in the second string.
    """
    # Read two input strings from the user
    string1 = input()
    string2 = input()

    # Remove spaces from both strings
    cleaned_string1 = string1.replace(" ", "")
    cleaned_string2 = string2.replace(" ", "")

    # Initialize an array to store the frequency difference
    frequency_differences = []

    # ASCII values range for uppercase 'A' (65) to lowercase 'z' (122)
    for x in range(65, 123):
        # Count the occurrences of the character represented by x in both strings
        count_in_string1 = cleaned_string1.count(chr(x))
        count_in_string2 = cleaned_string2.count(chr(x))
        
        # Calculate the difference in frequencies and store it in the array
        frequency_difference = count_in_string1 - count_in_string2
        frequency_differences.append(frequency_difference)

    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the main function
check_letter_frequencies()
