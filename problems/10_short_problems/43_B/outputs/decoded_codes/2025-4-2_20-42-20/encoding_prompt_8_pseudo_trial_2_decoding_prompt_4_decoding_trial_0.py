def can_transform_string():
    # Step 1: Gather Input Strings
    first_input = input()
    second_input = input()

    # Step 2: Process Strings to Remove Spaces
    first_string = [char for char in first_input if char != ' ']
    second_string = [char for char in second_input if char != ' ']

    # Step 3: Calculate Frequency Differences
    frequency_differences = [0] * (123)  # ASCII range from 0 to 122

    for char_code in range(65, 123):  # From 'A' (65) to 'z' (122)
        count_first = first_string.count(chr(char_code))
        count_second = second_string.count(chr(char_code))
        frequency_differences[char_code] = count_first - count_second

    # Step 4: Determine Validity of Transformation
    if all(diff >= 0 for diff in frequency_differences):
        # Step 5: Output the Result
        print("YES")
    else:
        print("NO")

# Invoke the function to execute
can_transform_string()
