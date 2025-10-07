def count_upper(s: str) -> int:
    count = 0
    length_of_s = len(s)
    index = 0
    while index < length_of_s:
        current_char = s[index]
        if current_char in ("A", "E", "I", "O", "U"):
            count += 1
        index += 2
    return count