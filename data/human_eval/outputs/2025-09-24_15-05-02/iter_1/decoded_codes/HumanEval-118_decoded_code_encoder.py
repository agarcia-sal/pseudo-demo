def get_closest_vowel(w):
    v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    if len(w) < 3:
        return ""
    for i in range(len(w) - 2, 0, -1):
        if w[i] in v and w[i-1] not in v and w[i+1] not in v:
            return w[i]
    return ""