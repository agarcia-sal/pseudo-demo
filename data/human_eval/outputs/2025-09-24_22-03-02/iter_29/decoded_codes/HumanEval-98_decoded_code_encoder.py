def count_upper(s):
    count = 0
    length = len(s)
    for i in range(0, length, 2):
        current_char = s[i]
        if current_char in {"A", "E", "I", "O", "U"}:
            count += 1
    return count