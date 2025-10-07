def count_upper(string_s: str) -> int:
    count: int = 0
    for index in range(0, len(string_s), 2):
        if string_s[index] in "AEIOU":
            count += 1
    return count