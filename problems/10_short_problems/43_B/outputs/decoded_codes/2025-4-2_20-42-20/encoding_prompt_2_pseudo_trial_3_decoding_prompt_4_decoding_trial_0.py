def main():
    # Step 1: Input two strings from the user
    string_one = input()
    string_two = input()

    # Step 2: Process the Strings to exclude spaces
    filtered_string_one = [char for char in string_one if char != ' ']
    filtered_string_two = [char for char in string_two if char != ' ']

    # Step 3: Count Character Frequencies
    # Initialize frequency difference list
    frequency_difference = [0] * 256  # Considering extended ASCII characters

    for char in filtered_string_one:
        frequency_difference[ord(char)] += 1  # Increment count for string_one

    for char in filtered_string_two:
        frequency_difference[ord(char)] -= 1  # Decrement count for string_two

    # Step 4: Check Frequency Conditions
    negative_counts = [count for count in frequency_difference if count < 0]

    # Prepare output based on the counts
    if not negative_counts:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
