def count_upper(s):
    return sum(1 if s[i] in "AEIOU" else 0 for i in range(0, len(s), 2))