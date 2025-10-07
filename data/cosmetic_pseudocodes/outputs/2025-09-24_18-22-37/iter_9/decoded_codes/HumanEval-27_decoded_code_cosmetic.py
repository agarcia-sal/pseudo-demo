def flip_case(alpha_sequence: str) -> str:
    beta_sequence = []
    delta_index = 0
    length = len(alpha_sequence)
    while delta_index < length:
        gamma_char = alpha_sequence[delta_index]
        if 'a' <= gamma_char <= 'z':
            gamma_char = chr(ord(gamma_char) - 32)
        elif 'A' <= gamma_char <= 'Z':
            gamma_char = chr(ord(gamma_char) + 32)
        beta_sequence.append(gamma_char)
        delta_index += 1
    return ''.join(beta_sequence)