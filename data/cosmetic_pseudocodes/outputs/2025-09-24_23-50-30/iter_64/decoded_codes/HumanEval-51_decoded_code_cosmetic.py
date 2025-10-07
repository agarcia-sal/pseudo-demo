def remove_vowels(omega: str) -> str:
    rho = ""
    upsilon = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while upsilon < len(omega):
        char = omega[upsilon]
        if char.lower() not in vowels:
            rho += char
        upsilon += 1
    return rho