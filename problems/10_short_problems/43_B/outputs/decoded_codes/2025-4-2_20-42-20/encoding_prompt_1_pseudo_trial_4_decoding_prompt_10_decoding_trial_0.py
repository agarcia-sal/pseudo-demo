def main():
    # Step 1: Input two strings and remove spaces
    first_string = input().replace(" ", "")
    second_string = input().replace(" ", "")

    # Step 2: Create a list to hold the character frequency differences
    frequency_difference = [0] * 256  # ASCII range

    # Counting frequency of each character in both strings
    for char in first_string:
        frequency_difference[ord(char)] += 1  # Increment frequency for first string

    for char in second_string:
        frequency_difference[ord(char)] -= 1  # Decrement frequency for second string

    # Step 3: Check for negative differences
    negative_count = sum(1 for diff in frequency_difference if diff < 0)

    # Output result based on negative counts
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
