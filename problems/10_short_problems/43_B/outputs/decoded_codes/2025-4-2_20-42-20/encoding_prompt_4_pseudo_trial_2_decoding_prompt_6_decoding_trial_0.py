# Define the function to check character frequencies
def check_character_frequencies():
    # Read two lines of input
    line_1 = input()
    line_2 = input()

    # Remove spaces and store characters in lists
    char_list_1 = [char for char in line_1 if char != ' ']
    char_list_2 = [char for char in line_2 if char != ' ']

    # Initialize a list to store frequency differences
    frequency_differences = []

    # Calculate frequency difference for each character from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):  # 65 is 'A', 122 is 'z'
        # Get character from code
        character = chr(char_code)

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

# Call the function to execute the character frequency check
check_character_frequencies()
