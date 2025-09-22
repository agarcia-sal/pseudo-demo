# Function to determine if the first string can be formed from the second string
def can_form_string_from_another():
    # Step 1: Read two strings from user input
    first_string = input()
    second_string = input()
    
    # Step 2: Remove spaces from both strings
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")

    # Step 3: Initialize a frequency list to store counts of character differences
    # The size is 128 to cover all ASCII characters
    character_frequency = [0] * 128

    # Step 4: Calculate the frequency of each character
    for char in range(65, 123):  # ASCII values for 'A' to 'z'
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

# You can call the function to test
# can_form_string_from_another()
