def character_frequency_check():
    # Initialize two lists to store characters from the inputs
    s1 = []
    s2 = []

    # Read user inputs
    first_input = input()
    second_input = input()

    # Populate s1 with non-space characters from first_input
    for char in first_input:
        if char != ' ':
            s1.append(char)

    # Populate s2 with non-space characters from second_input
    for char in second_input:
        if char != ' ':
            s2.append(char)

    # Initialize a list to store frequency differences
    freqs = []

    # Calculate frequency differences for each ASCII character from 'A' to 'z'
    for x in range(ord('A'), ord('z') + 1):
        # Count occurrences in both lists
        count_s1 = s1.count(chr(x))
        count_s2 = s2.count(chr(x))
        # Calculate frequency difference and store in freqs
        freqs.append(count_s1 - count_s2)

    # Count how many elements in freqs are less than 0
    negative_count = sum(1 for freq in freqs if freq < 0)

    # Output result based on counts
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the code
character_frequency_check()
