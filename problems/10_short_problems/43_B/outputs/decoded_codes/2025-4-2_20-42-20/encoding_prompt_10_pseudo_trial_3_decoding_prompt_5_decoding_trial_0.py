def main():
    # Step 2: Initialize lists to hold characters without spaces
    list_s1 = []
    list_s2 = []
    
    # Step 4: Read first input
    first_input = input()
    # Step 5: Read second input
    second_input = input()

    # Step 6: Process first input and store characters in list_s1
    for character in first_input:
        if character != ' ':
            list_s1.append(character)

    # Step 7: Process second input and store characters in list_s2
    for character in second_input:
        if character != ' ':
            list_s2.append(character)

    # Step 8: Initialize a list to store frequency differences
    frequency_differences = []

    # Step 9: Count character occurrences and calculate differences
    for ascii_value in range(ord('A'), ord('z') + 1):
        char_from_s1 = chr(ascii_value)
        count_s1 = list_s1.count(char_from_s1)
        count_s2 = list_s2.count(char_from_s1)
        difference = count_s1 - count_s2
        frequency_differences.append(difference)

    # Step 10: Count elements in frequency_differences that are less than 0
    negative_count = sum(1 for freq in frequency_differences if freq < 0)

    # Step 11: Check if negative_count is equal to 0
    if negative_count == 0:
        print("YES")  # Step 12: Output "YES"
    else:
        print("NO")   # Step 12: Output "NO"

# Call the main function to execute the program
main()
