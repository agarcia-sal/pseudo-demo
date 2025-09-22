def main():
    # Step 2: Initialize lists
    s1 = []
    s2 = []

    # Step 4: Read first input and store it in 'first_input'
    first_input = input()
    
    # Step 5: Read second input and store it in 'second_input'
    second_input = input()

    # Step 6: Process the first input to fill s1
    for character in first_input:
        if character != ' ':  # Step 6a
            s1.append(character)  # Step 6ai

    # Step 7: Process the second input to fill s2
    for character in second_input:
        if character != ' ':  # Step 7a
            s2.append(character)  # Step 7ai

    # Step 8: Initialize a list to store frequency differences
    freqs = []

    # Step 9: Calculate frequency differences for characters
    for x in range(ord('A'), ord('z') + 1):  # Step 9
        char = chr(x)
        count_s1 = s1.count(char)  # Count occurrences in s1
        count_s2 = s2.count(char)  # Count occurrences in s2
        freq_difference = count_s1 - count_s2  # Step 9c
        freqs.append(freq_difference)  # Store the result

    # Step 10: Count the number of elements in freqs that are less than 0
    negative_count = sum(1 for freq in freqs if freq < 0)  # Step 10

    # Step 11: Output result based on negative_count
    if negative_count == 0:  # Step 11
        print("YES")
    else:  # Step 12a
        print("NO")

# Step 1: Begin Program
if __name__ == "__main__":
    main()  # Execute the main function
