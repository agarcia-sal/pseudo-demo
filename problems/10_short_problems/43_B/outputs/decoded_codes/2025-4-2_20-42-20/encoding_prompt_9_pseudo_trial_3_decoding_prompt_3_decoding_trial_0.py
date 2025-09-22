def are_anagrams():
    # Step 1: Get User Input
    print("Enter the first string:")
    first_string = input()
    
    print("Enter the second string:")
    second_string = input()

    # Step 2: Remove Spaces
    string1 = first_string.replace(" ", "")
    string2 = second_string.replace(" ", "")

    # Step 3: Count Character Frequencies
    frequency_difference = []

    # Check ASCII range from 'A' (65) to 'z' (122)
    for ascii_char in range(65, 123):
        char = chr(ascii_char)
        count_in_first = string1.count(char)
        count_in_second = string2.count(char)
        diff = count_in_first - count_in_second
        frequency_difference.append(diff)

    # Step 4: Check Frequency Differences
    negative_count = sum(1 for count in frequency_difference if count < 0)

    # Step 5: Generate Output
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
are_anagrams()
