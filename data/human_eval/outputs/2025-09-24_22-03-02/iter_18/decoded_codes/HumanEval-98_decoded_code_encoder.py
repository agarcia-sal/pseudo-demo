def count_upper(s) -> int:
    count = 0
    length_of_s = len(s)
    i = 0
    while i < length_of_s:
        current_character = s[i]
        if current_character in ("A", "E", "I", "O", "U"):
            count += 1
        i += 2
    return count