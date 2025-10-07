def flip_case(delta: str) -> str:
    epsilon = ""
    zeta = 0
    while zeta < len(delta):
        char_omega = delta[zeta]
        is_upper = 'A' <= char_omega <= 'Z'
        is_lower = 'a' <= char_omega <= 'z'
        if is_upper:
            char_phi = chr(ord(char_omega) + (97 - 65))
            epsilon += char_phi
        else:
            if is_lower:
                char_sigma = chr(ord(char_omega) - (97 - 65))
                epsilon += char_sigma
            else:
                epsilon += char_omega
        zeta += 1
    return epsilon