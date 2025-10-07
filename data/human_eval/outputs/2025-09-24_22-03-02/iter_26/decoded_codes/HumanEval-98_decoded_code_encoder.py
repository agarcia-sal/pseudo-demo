def count_upper(s):
    count = 0
    i = 0
    vowels = "AEIOU"
    while i < len(s):
        if s[i] in vowels:
            count += 1
        i += 2
    return count