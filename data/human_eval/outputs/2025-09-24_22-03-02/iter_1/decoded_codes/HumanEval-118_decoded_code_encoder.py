def find_vowel(w):
    if len(w) < 3:
        return ""
    V = {"a","e","i","o","u","A","E","I","O","U"}
    for i in range(len(w)-2, 0, -1):
        if w[i] in V and w[i-1] not in V and w[i+1] not in V:
            return w[i]
    return ""