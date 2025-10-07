def select_words(s, n):
    return [w for w in s.split() if sum(1 for c in w.lower() if c not in "aeiou") == n]