# Define the main function to execute the string comparison
def compare_character_frequencies():
    # Step 1: Input the two strings
    first_string = input()  # Prompting the user for the first string
    second_string = input()  # Prompting the user for the second string

    # Step 2: Remove spaces and create lists of characters
    list1 = [char for char in first_string if char != ' ']  # List of characters in the first string excluding spaces
    list2 = [char for char in second_string if char != ' ']  # List of characters in the second string excluding spaces

    # Step 3: Initialize frequency difference list
    frequency_difference = []  # List to store differences in character counts

    # Step 4: Calculate frequency differences for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):  # Iterate through character codes from 'A' to 'z'
        # Count occurrences of the character in both lists
        character_count_in_first = list1.count(chr(character_code))  # Count in the first list
        character_count_in_second = list2.count(chr(character_code))  # Count in the second list
        
        # Calculate the difference and append to frequency_difference
        difference = character_count_in_first - character_count_in_second
        frequency_difference.append(difference)

    # Step 5: Check for negatives in frequency_difference
    negative_count = sum(1 for count in frequency_difference if count < 0)  # Count negative differences

    # Step 6: Output the result
    if negative_count == 0:  # If there are no negative values
        print("YES")
    else:
        print("NO")

# Run the function to execute the logic
compare_character_frequencies()
