def count_occurrences(target_char, character_list):
    """Counts occurrences of target_char in character_list."""
    count = 0
    for character in character_list:
        if character == target_char:
            count += 1
    return count

def main():
    # Step 1: Accept input
    first_string = input()
    second_string = input()

    # Step 2: Remove spaces from both strings
    cleaned_string1 = [char for char in first_string if char != ' ']
    cleaned_string2 = [char for char in second_string if char != ' ']

    # Step 3: Calculate frequency differences of characters
    frequency_differences = []
    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)
        count_in_first = count_occurrences(current_char, cleaned_string1)
        count_in_second = count_occurrences(current_char, cleaned_string2)
        frequency_differences.append(count_in_first - count_in_second)

    # Step 4: Check if there are any negative frequency differences
    has_negative_frequency = any(difference < 0 for difference in frequency_differences)

    # Step 5: Output result
    if not has_negative_frequency:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
