def main():
    # Step 2: Receive Input from User
    first_input = input()
    second_input = input()

    # Step 3: Initialize Lists
    s1 = [char for char in first_input if char != ' ']
    s2 = [char for char in second_input if char != ' ']

    # Step 4: Initialize Frequency Counter
    frequency_counter = [0] * 256  # for all ASCII values

    # Step 5: Calculate Character Frequencies
    for ascii_value in range(65, 123):  # from A (65) to z (122)
        count_in_s1 = s1.count(chr(ascii_value))
        count_in_s2 = s2.count(chr(ascii_value))
        # Calculate the difference
        frequency_counter[ascii_value] = count_in_s1 - count_in_s2

    # Step 6: Determine if Frequencies are Non-Negative
    negative_count = sum(1 for count in frequency_counter if count < 0)

    # Step 6: Print Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Step 1: Start Program
if __name__ == "__main__":
    main()
