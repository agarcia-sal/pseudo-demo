def check_character_distribution():
    # Step 1: Read two strings from user input
    firstString = input().replace(" ", "")
    secondString = input().replace(" ", "")

    # Step 2: Initialize an array to hold frequency differences
    frequency_differences = [0] * (ord('z') - ord('A') + 1)  # From 'A' to 'z'

    # Step 3: Calculate the frequency difference for each character
    for char in range(ord('A'), ord('z') + 1):
        count_first = firstString.count(chr(char))
        count_second = secondString.count(chr(char))
        frequency_differences[char - ord('A')] = count_first - count_second

    # Step 4: Check if any character has a negative frequency difference
    negative_count = 0
    for diff in frequency_differences:
        if diff < 0:
            negative_count += 1

    # Step 5: Determine if the character distributions are valid
    if negative_count == 0:
        print("YES")  # implying firstString can cover secondString
    else:
        print("NO")   # implying firstString cannot cover secondString

# Call the function to execute the logic
check_character_distribution()
