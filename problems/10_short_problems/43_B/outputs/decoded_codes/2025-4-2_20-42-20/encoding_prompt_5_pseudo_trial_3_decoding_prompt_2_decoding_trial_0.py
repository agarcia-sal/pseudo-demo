def compare_character_frequencies():
    # Step 1: Get input strings from the user
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")
    
    # Step 2: Initialize the frequency difference list
    frequency_differences = []

    # Step 3: Loop through ASCII values from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        # Count occurrences of the character in both strings
        count_in_first = first_string.count(chr(char_code))
        count_in_second = second_string.count(chr(char_code))

        # Calculate the difference in counts
        difference = count_in_first - count_in_second
        frequency_differences.append(difference)

    # Step 4: Check if all differences are greater than or equal to zero
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the function to execute the comparison
compare_character_frequencies()
