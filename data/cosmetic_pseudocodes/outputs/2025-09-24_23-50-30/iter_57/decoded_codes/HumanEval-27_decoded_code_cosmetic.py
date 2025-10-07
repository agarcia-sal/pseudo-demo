def flip_case(delta: str) -> str:
    epsilon = []
    for zeta in delta:
        if 'a' <= zeta <= 'z':
            eta = zeta.upper()
        elif 'A' <= zeta <= 'Z':
            eta = zeta.lower()
        else:
            eta = zeta
        epsilon.append(eta)
    return ''.join(epsilon)