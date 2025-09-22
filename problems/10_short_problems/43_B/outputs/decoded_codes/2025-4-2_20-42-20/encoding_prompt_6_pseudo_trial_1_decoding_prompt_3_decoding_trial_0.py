def check_character_distribution():
    # Step 1: Read two strings from user input
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")

    # Step 2: Initialize an array to hold frequency differences (for characters 'A' to 'z')
    frequency_differences = [0] * (ord('z') - ord('A') + 1)

    # Step 3: Calculate the frequency difference for each character
    for char in range(ord('A'), ord('z') + 1):
        count_first = first_string.count(chr(char))
        count_second = second_string.count(chr(char))
        frequency_differences[char - ord('A')] = count_first - count_second

    # Step 4: Check if any character has a negative frequency difference
    negative_difference_count = 0
    for difference in frequency_differences:
        if difference < 0:
            negative_difference_count += 1

    # Step 5: Determine if the character distributions are valid
    if negative_difference_count == 0:
        print("YES")  # implying first_string can cover second_string
    else:
        print("NO")   # implying first_string cannot cover second_string

# To test the function, you would call it and provide input
check_character_distribution()
