def count_upper(s):
    count = 0
    for index in range(0, len(s), 2):
        if s[index] in "AEIOU":
            count += 1
    return count