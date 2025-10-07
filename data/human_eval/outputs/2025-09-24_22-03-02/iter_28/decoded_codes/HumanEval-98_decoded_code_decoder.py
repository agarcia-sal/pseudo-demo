def count_upper(s: str) -> int:
    count = 0
    length_of_s = len(s)
    i = 0
    while i < length_of_s:
        current_character = s[i]
        if current_character == "A" or current_character == "E" or current_character == "I" or current_character == "O" or current_character == "U":
            count += 1
        i += 2
    return count