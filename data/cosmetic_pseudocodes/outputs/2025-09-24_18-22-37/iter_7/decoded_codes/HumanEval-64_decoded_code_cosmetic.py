def vowels_count(text_body: str) -> int:
    vowel_chars = "aeiouAEIOU"
    total_vowels = 0
    idx = 1
    while idx <= len(text_body):
        current_char = text_body[idx - 1]  # Adjust for 0-based indexing
        if vowel_chars.find(current_char) >= 0:
            total_vowels += 1
        idx += 1
    if text_body:
        last_char = text_body[-1]
        if last_char == 'y' or last_char == 'Y':
            total_vowels += 1
    return total_vowels