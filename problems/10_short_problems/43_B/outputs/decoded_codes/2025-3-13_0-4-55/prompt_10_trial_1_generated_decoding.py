def main():
    # Step 2: Receive Input from User
    first_input = input()
    second_input = input()

    # Step 3: Initialize Lists
    s1 = [char for char in first_input if char != ' ']
    s2 = [char for char in second_input if char != ' ']

    # Step 4: Initialize Frequency Counter
    frequency_counter = [0] * 256  # Covers ASCII range

    # Step 5: Calculate Character Frequencies
    for x in range(65, 123):  # ASCII values from A (65) to z (122)
        count_in_s1 = s1.count(chr(x))
        count_in_s2 = s2.count(chr(x))
        frequency_counter[x] = count_in_s1 - count_in_s2

    # Step 6: Determine if Frequencies are Non-Negative
    negative_count = sum(1 for count in frequency_counter if count < 0)

    # Checking if there are any negative elements
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Step 1: Start Program
if __name__ == "__main__":
    main()
