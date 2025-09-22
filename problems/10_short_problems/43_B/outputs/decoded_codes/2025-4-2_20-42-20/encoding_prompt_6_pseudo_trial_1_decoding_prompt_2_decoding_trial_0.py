def check_character_distribution():
    # Step 1: Read two strings from user input
    firstString = input().replace(" ", "")
    secondString = input().replace(" ", "")
    
    # Step 2: Initialize an array to hold frequency differences
    freq_diff = [0] * (ord('z') - ord('A') + 1)  # Array to hold frequency differences for 'A' to 'z'

    # Step 3: Calculate the frequency difference for each character
    for char in range(ord('A'), ord('z') + 1):
        count_first = firstString.count(chr(char))
        count_second = secondString.count(chr(char))
        freq_diff[char - ord('A')] = count_first - count_second

    # Step 4: Check if any character has a negative frequency difference
    negative_diff_count = 0
    for diff in freq_diff:
        if diff < 0:
            negative_diff_count += 1

    # Step 5: Determine if the character distributions are valid
    if negative_diff_count == 0:
        print("YES")  # implying firstString can cover secondString
    else:
        print("NO")   # implying firstString cannot cover secondString

# Example usage
check_character_distribution()
