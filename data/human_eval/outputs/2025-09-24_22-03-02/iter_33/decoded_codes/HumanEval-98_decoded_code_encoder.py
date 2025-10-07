def count_upper(s) -> int:
    count = 0
    length = len(s)
    i = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while i < length:
        current_char = s[i]
        if current_char in vowels:
            count += 1
        i += 2
    return count