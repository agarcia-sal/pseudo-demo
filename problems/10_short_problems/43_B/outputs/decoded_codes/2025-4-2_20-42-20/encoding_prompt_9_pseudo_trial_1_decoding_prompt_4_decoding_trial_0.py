def can_transform():
    # Step 1: Retrieve Input
    first_string = input()
    second_string = input()
    
    # Step 2: Preprocess Input
    cleaned_strings = [
        first_string.replace(" ", ""),  # Remove spaces from the first string
        second_string.replace(" ", "")   # Remove spaces from the second string
    ]
    s1 = cleaned_strings[0]
    s2 = cleaned_strings[1]

    # Step 3: Count Character Frequencies
    frequency_difference = []
    
    for char in range(ord('A'), ord('z') + 1):  # Iterate through ASCII values from 'A' to 'z'
        count_s1 = s1.count(chr(char))
        count_s2 = s2.count(chr(char))
        frequency_difference.append(count_s1 - count_s2)  # Calculate the difference

    # Step 4: Check Character Count Requirements
    negative_count = len([diff for diff in frequency_difference if diff < 0])  # Count negatives

    # Step 5: Provide Output
    if negative_count == 0:
        print("YES")  # Transformation is possible
    else:
        print("NO")   # Transformation is not possible

# Call the function to run the transformation check
can_transform()
