def are_anagrams():
    # Step 1: Get User Input
    first_string = input()
    second_string = input()

    # Step 2: Remove Spaces
    string1 = first_string.replace(" ", "")
    string2 = second_string.replace(" ", "")

    # Step 3: Count Character Frequencies
    frequency_difference = []

    # Loop through ASCII values from 'A' (65) to 'z' (122)
    for ascii_value in range(65, 123):
        char = chr(ascii_value)
        count_in_first = string1.count(char)
        count_in_second = string2.count(char)
        diff = count_in_first - count_in_second
        frequency_difference.append(diff)

    # Step 4: Check Frequency Differences
    negative_count = sum(1 for diff in frequency_difference if diff < 0)

    # Step 5: Generate Output
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
are_anagrams()
