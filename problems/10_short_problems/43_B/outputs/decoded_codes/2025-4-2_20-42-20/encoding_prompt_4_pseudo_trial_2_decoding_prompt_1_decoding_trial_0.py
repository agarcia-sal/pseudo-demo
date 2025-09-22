def check_character_frequencies():
    # Read two lines of input
    LINE_1 = input()
    LINE_2 = input()

    # Remove spaces and store characters in lists
    CHAR_LIST_1 = [char for char in LINE_1 if char != ' ']
    CHAR_LIST_2 = [char for char in LINE_2 if char != ' ']

    # Initialize a list to store frequency differences
    FREQUENCY_DIFFERENCES = []

    # Calculate frequency difference for each character from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):  # 123 is exclusive
        # Get character from code
        CHARACTER = chr(char_code)

        # Count occurrences in both character lists
        COUNT_IN_LIST_1 = CHAR_LIST_1.count(CHARACTER)
        COUNT_IN_LIST_2 = CHAR_LIST_2.count(CHARACTER)

        # Append the difference to the frequency list
        FREQUENCY_DIFFERENCES.append(COUNT_IN_LIST_1 - COUNT_IN_LIST_2)

    # Check if all frequency differences are non-negative
    if all(difference >= 0 for difference in FREQUENCY_DIFFERENCES):
        print("YES")
    else:
        print("NO")

# You would typically call the function like this to execute:
# check_character_frequencies()
