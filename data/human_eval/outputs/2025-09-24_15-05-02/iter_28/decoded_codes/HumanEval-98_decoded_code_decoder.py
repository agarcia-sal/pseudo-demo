def count_upper(string_s: str) -> int:
    count = 0
    vowels = "AEIOU"
    for index in range(0, len(string_s), 2):
        if string_s[index] in vowels:
            count += 1
    return count