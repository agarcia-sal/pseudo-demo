def main():
    # Step 2: Receive Input from User
    first_input = input()  # Get the first input string from the user
    second_input = input()  # Get the second input string from the user

    # Step 3: Initialize Lists
    # Populate lists with non-space characters from the inputs
    s1 = [char for char in first_input if char != ' ']
    s2 = [char for char in second_input if char != ' ']

    # Step 4: Initialize Frequency Counter
    # List to count character occurrences for ASCII values
    frequency = [0] * 256

    # Step 5: Calculate Character Frequencies
    for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
        count_in_s1 = s1.count(chr(ascii_value))
        count_in_s2 = s2.count(chr(ascii_value))
        frequency[ascii_value] = count_in_s1 - count_in_s2

    # Step 6: Determine if Frequencies are Non-Negative
    # Count how many elements in frequency are negative
    negative_count = sum(1 for count in frequency if count < 0)

    if negative_count == 0:
        print("YES")  # All frequencies are non-negative
    else:
        print("NO")  # There are negative frequencies

# Entry point for the program
if __name__ == "__main__":
    main()
