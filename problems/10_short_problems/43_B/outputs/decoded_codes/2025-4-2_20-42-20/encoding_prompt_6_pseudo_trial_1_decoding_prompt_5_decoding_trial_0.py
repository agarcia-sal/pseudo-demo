def check_character_distribution():
    # Step 1: Read two strings from user input
    first_string = input().replace(" ", "")  # Read first string and remove spaces
    second_string = input().replace(" ", "")  # Read second string and remove spaces

    # Step 2: Initialize an array to hold frequency differences
    frequency_differences = [0] * (ord('z') - ord('A') + 1)  # Array to hold the frequency differences for characters A to z

    # Step 3: Calculate the frequency difference for each character
    for char in range(ord('A'), ord('z') + 1):  # Loop through each character from A to z
        count_first = first_string.count(chr(char))  # Count occurrences in first_string
        count_second = second_string.count(chr(char))  # Count occurrences in second_string
        frequency_differences[char - ord('A')] = count_first - count_second  # Store the frequency difference

    # Step 4: Check if any character has a negative frequency difference
    negative_difference_count = 0  # Initialize counter for negative differences
    for difference in frequency_differences:  # Loop through frequency differences
        if difference < 0:  # Check for negative differences
            negative_difference_count += 1  # Increment the count of negative differences

    # Step 5: Determine if the character distributions are valid
    if negative_difference_count == 0:  # If no negative differences found
        print("YES")  # first_string can cover second_string
    else:
        print("NO")  # first_string cannot cover second_string

# Note: Consider edge cases by providing test cases in comments
# These can include empty strings or strings containing only spaces
# check_character_distribution() could be called to test the function interactively.
