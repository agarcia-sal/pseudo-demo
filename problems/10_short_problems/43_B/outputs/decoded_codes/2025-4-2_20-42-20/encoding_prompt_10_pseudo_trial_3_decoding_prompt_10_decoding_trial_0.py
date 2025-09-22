def main():
    # Step 2: Initialize a list for first string characters
    s1 = []
    # Step 3: Initialize a list for second string characters
    s2 = []

    # Step 4: Read first input
    first_input = input()
    # Step 5: Read second input
    second_input = input()

    # Step 6: Process first input to populate s1
    for character in first_input:
        if character != ' ':
            s1.append(character)

    # Step 7: Process second input to populate s2
    for character in second_input:
        if character != ' ':
            s2.append(character)

    # Step 8: Initialize a list to store frequency differences
    freqs = []

    # Step 9: Count frequency differences for each character 'A' (65) to 'z' (122)
    for ascii_value in range(65, 123):
        count_s1 = s1.count(chr(ascii_value))
        count_s2 = s2.count(chr(ascii_value))
        freq_difference = count_s1 - count_s2
        freqs.append(freq_difference)

    # Step 10: Count how many elements in freqs are less than 0
    negative_count = sum(1 for freq in freqs if freq < 0)

    # Step 11: Determine output based on the negative_count
    if negative_count == 0:
        print("YES")  # Step 12a
    else:
        print("NO")   # Step 12b

# Run the main function
if __name__ == "__main__":
    main()
