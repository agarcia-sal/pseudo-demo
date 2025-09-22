def check_character_frequency():
    # Step 1: Read two input strings from the user
    first_string = input()
    second_string = input()
    
    # Step 2: Remove all spaces from both input strings
    first_cleaned_string = remove_spaces_from_string(first_string)
    second_cleaned_string = remove_spaces_from_string(second_string)

    # Step 3: Initialize a list to hold the frequency difference of characters
    character_frequency_difference = []

    # Step 4: Iterate through the ASCII values of uppercase and lowercase letters
    for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
        # Step 5: Count the occurrences of the character in both cleaned strings
        character = convert_ascii_to_character(ascii_value)
        count_in_first_string = count_occurrences(first_cleaned_string, character)
        count_in_second_string = count_occurrences(second_cleaned_string, character)

        # Step 6: Calculate the frequency difference and store it in the list
        difference = count_in_first_string - count_in_second_string
        character_frequency_difference.append(difference)

    # Step 7: Check if there are any negative differences
    negative_differences_count = count_elements_less_than_zero(character_frequency_difference)

    # Step 8: Output the result based on the negative differences count
    if negative_differences_count == 0:
        print("YES")
    else:
        print("NO")

def remove_spaces_from_string(input_string):
    # Remove spaces from the input string and return the cleaned string
    return input_string.replace(" ", "")

def count_occurrences(target_string, character):
    # Count how many times 'character' appears in 'targetString' and return the count
    return target_string.count(character)

def count_elements_less_than_zero(number_list):
    # Count how many elements in 'numberList' are less than zero
    return sum(1 for num in number_list if num < 0)

def convert_ascii_to_character(ascii_value):
    # Convert an ASCII value to its corresponding character
    return chr(ascii_value)

# Call the main function to execute the program
check_character_frequency()
