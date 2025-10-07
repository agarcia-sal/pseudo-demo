def count_upper(s: str) -> int:
    count = 0
    i = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while i < len(s):
        if s[i] in vowels:
            count += 1
        i += 2
    return count