def compare_strings():
    # Step 1: Read two strings from user input
    first_string = input()
    second_string = input()

    # Step 2: Remove spaces from both strings
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    
    # Step 3: Initialize a frequency list to store counts of character differences
    character_frequency = [0] * 256  # 256 to cover all ASCII characters

    # Step 4: Calculate the frequency of each character
    for char in range(65, 123):  # ASCII 'A' (65) to 'z' (122) inclusive
        count_in_first_string = first_string.count(chr(char))
        count_in_second_string = second_string.count(chr(char))
        
        # Calculate the difference in counts and store it in characterFrequency
        character_frequency[char] = count_in_first_string - count_in_second_string

    # Step 5: Check if all frequency differences are non-negative
    is_valid = True
    for count in character_frequency:
        if count < 0:
            is_valid = False
            break  # No need to check further, exit loop

    # Step 6: Output result based on validity check
    if is_valid:
        print("YES")
    else:
        print("NO")

# Call the function to execute the comparison
compare_strings()
