def compare_string_frequencies():
    # Step 1: Read two input strings from the user, stripping out any whitespace
    string1 = input().strip()
    string2 = input().strip()

    # Step 2: Create lists of characters without spaces for both strings
    characters_from_string1 = list(string1.replace(" ", ""))
    characters_from_string2 = list(string2.replace(" ", ""))

    # Step 3: Initialize a frequency list to store the difference in character counts
    frequency_differences = [0] * (ord('z') - ord('A') + 1)

    # Step 4: Calculate the frequency differences for each character
    for char_code in range(ord('A'), ord('z') + 1):
        count_in_first_string = characters_from_string1.count(chr(char_code))
        count_in_second_string = characters_from_string2.count(chr(char_code))
        frequency_differences[char_code - ord('A')] = count_in_first_string - count_in_second_string

    # Step 5: Check if all frequency differences are non-negative
    negative_frequencies = [freq for freq in frequency_differences if freq < 0]

    # Step 6: Determine the result based on the counts of negative frequencies
    if len(negative_frequencies) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_string_frequencies()
