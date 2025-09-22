def check_character_distribution():
    # Step 1: Read two strings from user input
    first_string = input().replace(" ", "")  # Removing spaces
    second_string = input().replace(" ", "")  # Removing spaces

    # Step 2: Initialize an array to hold frequency differences
    # ASCII values for 'A' (65) to 'z' (122)
    frequency_differences = [0] * (123)  # Total of 123 to cover all ASCII characters from A to z

    # Step 3: Calculate the frequency difference for each character
    for char in range(65, 123):  # ASCII 'A' to 'z'
        count_first = first_string.count(chr(char))
        count_second = second_string.count(chr(char))
        frequency_differences[char] = count_first - count_second

    # Step 4: Check if any character has a negative frequency difference
    negative_count = 0
    for diff in frequency_differences:
        if diff < 0:
            negative_count += 1

    # Step 5: Determine if the character distributions are valid
    if negative_count == 0:
        print("YES")  # first_string can cover second_string
    else:
        print("NO")   # first_string cannot cover second_string

# Example usage:
# This function will be called to execute the logic.
check_character_distribution()
