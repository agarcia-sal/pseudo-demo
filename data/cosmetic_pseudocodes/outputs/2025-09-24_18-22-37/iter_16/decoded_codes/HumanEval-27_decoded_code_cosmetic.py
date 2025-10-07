def flip_case(xylon: str) -> str:
    omega = []
    delta = 0
    while delta < len(xylon):
        psi = xylon[delta]
        if psi.isupper():
            lam = psi.lower()
        elif psi.islower():
            lam = psi.upper()
        else:
            lam = psi
        omega.append(lam)
        delta += 1
    return ''.join(omega)