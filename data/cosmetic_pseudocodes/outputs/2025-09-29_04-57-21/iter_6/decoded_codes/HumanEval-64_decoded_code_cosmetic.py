def vowels_count(text: str) -> int:
    vowels_letters: str = "aeiouAEIOU"
    total_vowels: int = 0
    for letter in text:
        if letter in vowels_letters:
            total_vowels += 1
    if text and text[-1] in {'Y', 'y'}:
        total_vowels += 1
    return total_vowels