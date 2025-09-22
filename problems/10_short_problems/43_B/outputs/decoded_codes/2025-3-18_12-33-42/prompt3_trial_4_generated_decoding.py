def are_anagrams():
    # Step 1: Get input from the user
    first_string = input()
    second_string = input()

    # Step 2: Create lists by filtering out spaces
    filtered_first_string = [character for character in first_string if character != ' ']
    filtered_second_string = [character for character in second_string if character != ' ']

    # Step 3: Initialize frequency difference list
    frequency_differences = []

    # Step 4: Calculate frequency differences for all characters
    for character_code in range(ord('A'), ord('z') + 1):  # From 'A' to 'z'
        count_in_first_string = filtered_first_string.count(chr(character_code))
        count_in_second_string = filtered_second_string.count(chr(character_code))
        
        # Compute the difference in frequency
        frequency_differences.append(count_in_first_string - count_in_second_string)

    # Step 5: Check if the frequency differences indicate an anagram
    is_anagram = True

    for frequency in frequency_differences:
        if frequency < 0:
            is_anagram = False
            break

    # Step 6: Output the result
    if is_anagram:
        print("YES")
    else:
        print("NO")

# Call the function to run the anagram check
are_anagrams()
