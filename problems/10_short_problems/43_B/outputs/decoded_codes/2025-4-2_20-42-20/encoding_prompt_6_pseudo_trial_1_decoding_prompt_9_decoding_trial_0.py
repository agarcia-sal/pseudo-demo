def check_character_distribution():
    # Step 1: Read two strings from user input
    first_string = input().replace(" ", "")  # Remove spaces from the first string
    second_string = input().replace(" ", "")  # Remove spaces from the second string

    # Step 2: Initialize a list to hold frequency differences (for 'A' to 'z')
    frequency_differences = [0] * (ord('z') - ord('A') + 1)

    # Step 3: Calculate the frequency difference for each character
    for char in range(ord('A'), ord('z') + 1):  # Loop through ASCII values for 'A' to 'z'
        count_first = first_string.count(chr(char))  # Count occurrences in the first string
        count_second = second_string.count(chr(char))  # Count occurrences in the second string
        frequency_differences[char - ord('A')] = count_first - count_second  # Store the difference

    # Step 4: Check if any character has a negative frequency difference
    negative_difference_count = 0
    for difference in frequency_differences:
        if difference < 0:  # If the difference is negative
            negative_difference_count += 1  # Increment the count of negative differences

    # Step 5: Determine if the character distributions are valid
    if negative_difference_count == 0:  # All frequencies are sufficient
        print("YES")  # first_string can cover second_string
    else:
        print("NO")  # first_string cannot cover second_string

