def vowels_count(s: str) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = 0
    for i in range(len(s)):
        c = s[i]
        is_vowel = False
        for j in range(len(vowels)):
            if c == vowels[j]:
                is_vowel = True
                break
        if is_vowel:
            n_vowels += 1
    if len(s) > 0:
        last_char = s[-1]
        if last_char == "y" or last_char == "Y":
            n_vowels += 1
    return n_vowels