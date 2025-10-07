def flip_case(delta_string: str) -> str:
    omega_string = []
    chi_index = 0
    while chi_index < len(delta_string):
        upsilon_char = delta_string[chi_index]
        if 'a' <= upsilon_char <= 'z':
            theta_val = ord(upsilon_char) - 32
            omega_string.append(chr(theta_val))
        elif 'A' <= upsilon_char <= 'Z':
            sigma_val = ord(upsilon_char) + 32
            omega_string.append(chr(sigma_val))
        else:
            omega_string.append(upsilon_char)
        chi_index += 1
    return ''.join(omega_string)