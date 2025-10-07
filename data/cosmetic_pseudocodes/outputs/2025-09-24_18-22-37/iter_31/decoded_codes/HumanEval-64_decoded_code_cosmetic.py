def vowels_count(text_parameter: str) -> int:
    vowel_chars = "aeiouAEIOU"
    total_vowels = 0
    position_tracker = 1  # 1-based indexing per pseudocode

    while position_tracker <= len(text_parameter):
        current_char = text_parameter[position_tracker - 1]  # adjust for 0-based indexing
        if current_char in vowel_chars:
            total_vowels += 1
        position_tracker += 1

    if text_parameter and text_parameter[-1] in {'Y', 'y'}:
        total_vowels += 1

    return total_vowels