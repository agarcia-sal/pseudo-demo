def remove_vowels(u: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    v = ''
    w = 0
    while w < len(u):
        x = u[w]
        if x.lower() not in vowels:
            v += x
        w += 1
    return v