def flip_case(echoed_alpha: str) -> str:
    kappa_string: str = ""
    iota_index: int = 0
    while iota_index < len(echoed_alpha):
        lambda_char: str = echoed_alpha[iota_index]
        mu_char: str = lambda_char
        if "a" <= lambda_char <= "z":
            mu_char = chr(ord(lambda_char) - 32)
        elif "A" <= lambda_char <= "Z":
            mu_char = chr(ord(lambda_char) + 32)
        kappa_string += mu_char
        iota_index += 1
    return kappa_string