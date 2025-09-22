def check_character_distribution():
    # Step 1: Read two strings from user input
    firstString = input().replace(" ", "")  # Read first string and remove spaces
    secondString = input().replace(" ", "")  # Read second string and remove spaces

    # Step 2: Initialize an array to hold frequency differences (for ASCII characters)
    frequency_differences = [0] * (ord('z') - ord('A') + 1)  # Total 58 characters from 'A' to 'z'

    # Step 3: Calculate the frequency difference for each character
    for char in range(ord('A'), ord('z') + 1):  # Loop over ASCII values from 'A' to 'z'
        count_first = firstString.count(chr(char))  # Count occurrences in firstString
        count_second = secondString.count(chr(char))  # Count occurrences in secondString
        frequency_differences[char - ord('A')] = count_first - count_second  # Store the difference

    # Step 4: Check if any character has a negative frequency difference
    negative_count = 0  # Initialize counter for negative differences
    for diff in frequency_differences:
        if diff < 0:  # If any difference is negative, increment the count
            negative_count += 1

    # Step 5: Determine if the character distributions are valid
    if negative_count == 0:  # If there are no negative differences
        print("YES")  # firstString can cover secondString
    else:
        print("NO")   # firstString cannot cover secondString

# To execute the function
check_character_distribution()
