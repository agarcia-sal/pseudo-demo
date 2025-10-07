def count_upper(s: str) -> int:
    count = 0
    length = len(s)
    i = 0
    while i < length:
        current_char = s[i]
        if current_char == "A" or current_char == "E" or current_char == "I" or current_char == "O" or current_char == "U":
            count += 1
        i += 2
    return count