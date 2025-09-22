def main():
    # Step 1: Read input
    first_string = input()
    second_string = input()

    # Step 2: Remove spaces from both strings
    filtered_first_string = [char for char in first_string if char != ' ']
    filtered_second_string = [char for char in second_string if char != ' ']

    # Step 3: Count character frequency differences
    frequency_differences = []

    # ASCII values for 'A' (65) to 'z' (122)
    for char_code in range(65, 123):
        character = chr(char_code)
        count_in_first_string = filtered_first_string.count(character)
        count_in_second_string = filtered_second_string.count(character)
        difference = count_in_first_string - count_in_second_string
        frequency_differences.append(difference)

    # Step 4: Check if any frequency difference is negative
    has_negative_difference = any(difference < 0 for difference in frequency_differences)

    # Step 5: Output the result
    if not has_negative_difference:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
