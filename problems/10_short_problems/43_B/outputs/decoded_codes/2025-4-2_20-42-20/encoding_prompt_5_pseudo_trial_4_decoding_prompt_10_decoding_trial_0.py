def compare_strings():
    # Read user input and remove spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")

    # Initialize frequency dictionary to count character occurrences
    frequency_differences = {}

    # Count frequencies for characters in the first string
    for char in first_string:
        if char in frequency_differences:
            frequency_differences[char] += 1
        else:
            frequency_differences[char] = 1

    # Subtract frequencies for characters in the second string
    for char in second_string:
        if char in frequency_differences:
            frequency_differences[char] -= 1
        else:
            frequency_differences[char] = -1

    # Check for any negative counts in the frequency differences
    can_match = all(count >= 0 for count in frequency_differences.values())

    # Output result
    if can_match:
        print("YES")
    else:
        print("NO")

# Call the function to execute the comparison
compare_strings()
