def count_upper(s: str) -> int:
    count = 0
    length_s = len(s)
    i = 0
    while i < length_s:
        current_char = s[i]
        if current_char in ("A", "E", "I", "O", "U"):
            count += 1
        i += 2
    return count