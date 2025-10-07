def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    index = 0
    while index < len(s):
        c = s[index]
        is_in_vowels = False
        vowels_index = 0
        while vowels_index < len(vowels):
            if c == vowels[vowels_index]:
                is_in_vowels = True
                break
            vowels_index += 1
        if is_in_vowels:
            n_vowels += 1
        index += 1
    last_char = s[len(s) - 1]
    if last_char == "y" or last_char == "Y":
        n_vowels += 1
    return n_vowels