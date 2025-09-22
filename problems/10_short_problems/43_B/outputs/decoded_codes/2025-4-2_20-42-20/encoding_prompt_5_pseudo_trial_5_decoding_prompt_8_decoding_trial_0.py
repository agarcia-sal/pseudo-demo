def compare_character_frequencies():
    first_string = input()
    second_string = input()

    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")

    frequency_list = []

    for character_code in range(ord('A'), ord('z') + 1):
        frequency_first = cleaned_first_string.count(chr(character_code))
        frequency_second = cleaned_second_string.count(chr(character_code))
        difference = frequency_first - frequency_second
        frequency_list.append(difference)

    negative_count = sum(1 for difference in frequency_list if difference < 0)

    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# This function can be tested with various input scenarios and edge cases:
# Test cases could include:
# 1. Equal character counts in both strings
# 2. Additional characters in the second string
# 3. Missing characters in the second string
# 4. Case sensitivity (e.g., 'a' and 'A')
# 5. Strings with spaces

# Example calls for testing:
# compare_character_frequencies()  # Input for testing can be done interactively


from collections import Counter

def compare_character_frequencies() -> None:
    """Compares character frequencies in two input strings and determines if all characters in the first string are present in the second string."""
    first_string = input()
    second_string = input()

    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")

    first_counter = Counter(cleaned_first_string)
    second_counter = Counter(cleaned_second_string)

    for char in first_counter:
        if first_counter[char] > second_counter.get(char, 0):
            print("NO")
            return

    print("YES")
