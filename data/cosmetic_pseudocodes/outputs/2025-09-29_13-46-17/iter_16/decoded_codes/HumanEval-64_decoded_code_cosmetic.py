from typing import Optional

def vowels_count(string_input: str) -> int:
    vowels = "aeiouAEIOU"

    def check_vowel(char: Optional[str], _: Optional[object]) -> int:
        return 1 if char in vowels else 0

    # Adds counts for the first and second character if present (based on original logic)
    first_char_count = check_vowel(string_input[0], None) if string_input else 0
    second_char_count = check_vowel(string_input[1], None) if len(string_input) > 1 else 0

    def count_vowels(s: str, acc: int) -> int:
        if s == "":
            return acc
        head = s[0]
        return count_vowels(s[1:], acc + (1 if head in vowels else 0))

    total = count_vowels(string_input, 0)

    if string_input and (string_input[-1] == "y" or string_input[-1] == "Y"):
        total += 1

    return total