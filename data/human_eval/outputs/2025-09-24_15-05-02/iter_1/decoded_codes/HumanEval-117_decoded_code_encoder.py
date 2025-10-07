def select_words(s, n):
    return [w for w in s.split() if sum(c.lower() not in "aeiou" for c in w) == n]