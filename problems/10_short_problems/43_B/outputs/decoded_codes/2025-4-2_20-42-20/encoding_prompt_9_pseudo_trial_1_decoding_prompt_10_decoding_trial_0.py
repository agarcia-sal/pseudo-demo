def can_transform_strings():
    # Step 1: Retrieve Input
    first_string = input()
    second_string = input()

    # Step 2: Preprocess Input
    cleaned_strings = [
        first_string.replace(" ", ""),  # Remove spaces from first string
        second_string.replace(" ", "")  # Remove spaces from second string
    ]
    
    s1 = cleaned_strings[0]
    s2 = cleaned_strings[1]

    # Step 3: Count Character Frequencies
    frequency_difference = []
    
    # Loop through ASCII values from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):  # 'A' to 'z'
        char = chr(char_code)
        count_s1 = s1.count(char)
        count_s2 = s2.count(char)
        # Calculate the difference in count
        difference = count_s1 - count_s2
        frequency_difference.append(difference)

    # Step 4: Check Character Count Requirements
    insufficient_count = sum(1 for diff in frequency_difference if diff < 0)

    # Step 5: Provide Output
    if insufficient_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the string transformation check
can_transform_strings()
