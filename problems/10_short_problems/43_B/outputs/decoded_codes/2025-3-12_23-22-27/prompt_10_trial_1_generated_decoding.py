def main():
    # Step 2: Receive input from user
    first_input = input()
    second_input = input()

    # Step 3: Initialize lists excluding spaces
    s1 = [char for char in first_input if char != ' ']
    s2 = [char for char in second_input if char != ' ']

    # Step 4: Initialize frequency counter
    frequency = [0] * 256  # Support for all ASCII characters

    # Step 5: Calculate character frequencies
    for x in range(65, 123):  # ASCII range from 'A' (65) to 'z' (122)
        frequency[x] = s1.count(chr(x)) - s2.count(chr(x))

    # Step 6: Determine if frequencies are non-negative
    negative_count = sum(1 for count in frequency if count < 0)

    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
