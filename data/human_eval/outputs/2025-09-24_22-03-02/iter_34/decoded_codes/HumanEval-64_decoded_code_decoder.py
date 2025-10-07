def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = 0
    length_s = len(s)
    for i in range(length_s):
        c = s[i]
        j = 0
        found = False
        while j < len(vowels) and not found:
            if c == vowels[j]:
                found = True
            j += 1
        if found:
            n_vowels += 1
    if length_s > 0:
        last_char = s[length_s - 1]
        if last_char == "y" or last_char == "Y":
            n_vowels += 1
    return n_vowels