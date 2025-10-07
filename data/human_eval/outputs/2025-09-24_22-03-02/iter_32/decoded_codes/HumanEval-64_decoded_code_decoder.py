def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    for i in range(len(s)):
        c = s[i]
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
            n_vowels += 1
    last_index = len(s) - 1
    if last_index >= 0:
        last_char = s[last_index]
        if last_char == 'y' or last_char == 'Y':
            n_vowels += 1
    return n_vowels