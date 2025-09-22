def check_character_frequencies():
    # Read two lines of input
    line_1 = input()
    line_2 = input()

    # Remove spaces and store characters in lists
    char_list_1 = [char for char in line_1 if char != ' ']
    char_list_2 = [char for char in line_2 if char != ' ']

    # Initialize a list to store frequency differences
    frequency_differences = []

    # Calculate frequency difference for each character from 'A' to 'z'
    for char_code in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
        character = chr(char_code)  # Get character from code
        
        # Count occurrences in both character lists
        count_in_list_1 = char_list_1.count(character)
        count_in_list_2 = char_list_2.count(character)
        
        # Append the difference to the frequency list
        frequency_differences.append(count_in_list_1 - count_in_list_2)

    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# To call the function, uncomment the following line:
# check_character_frequencies()
