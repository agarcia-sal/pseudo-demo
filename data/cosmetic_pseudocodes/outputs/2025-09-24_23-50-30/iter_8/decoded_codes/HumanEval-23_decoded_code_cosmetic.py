def strlen(s: str) -> int:
    length_counter = 0
    while True:
        if length_counter >= len(s) or s[length_counter] == '\0':
            break
        length_counter += 1
    return length_counter