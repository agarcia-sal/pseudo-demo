def compare_character_frequencies():
    # Step 1: Input the two strings
    first_string = input()
    second_string = input()

    # Step 2: Remove spaces and create character lists
    list1 = [char for char in first_string if char != ' ']  # Remove spaces from first string
    list2 = [char for char in second_string if char != ' ']  # Remove spaces from second string

    # Step 3: Initialize frequency difference list
    frequency_difference = []

    # Step 4: Calculate frequency differences for each character A to z
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)
        character_count_in_first = list1.count(character)
        character_count_in_second = list2.count(character)
        difference = character_count_in_first - character_count_in_second
        frequency_difference.append(difference)

    # Step 5: Check for negatives in frequency difference
    negative_count = sum(1 for diff in frequency_difference if diff < 0)

    # Step 6: Output the result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to run the program
compare_character_frequencies()
