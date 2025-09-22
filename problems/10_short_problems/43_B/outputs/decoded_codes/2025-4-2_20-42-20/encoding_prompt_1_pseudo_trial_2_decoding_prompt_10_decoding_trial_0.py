def check_character_frequencies():
    # Step 1: Read input strings
    first_string = input()
    second_string = input()

    # Step 2: Process the strings and filter out spaces
    filtered_first = [char for char in first_string if char != ' ']
    filtered_second = [char for char in second_string if char != ' ']

    # Step 3: Initialize frequency differences
    frequency_differences = []
    # Iterate over ASCII values from 'A' (65) to 'z' (122)
    for ascii_value in range(65, 123):
        char = chr(ascii_value)
        count_first = filtered_first.count(char)
        count_second = filtered_second.count(char)
        frequency_differences.append(count_first - count_second)

    # Step 4: Check for negative frequencies
    negative_frequencies = [diff for diff in frequency_differences if diff < 0]
    negative_count = len(negative_frequencies)

    # Step 5: Output result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Run the function to check character frequencies
check_character_frequencies()
