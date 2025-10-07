from typing import Dict

def encode(parameter_lambda: str) -> str:
    flag_phi: str = "AEIOUaeiou"
    map_theta: Dict[str, str] = {}

    for value_sigma in flag_phi:
        key_psi: str = value_sigma
        char_chi: str = chr(ord(key_psi) + 2)
        map_theta[key_psi] = char_chi

    temporal_beta: str = ""
    index_mu: int = 0

    while index_mu < len(parameter_lambda):
        char_eta: str = parameter_lambda[index_mu]
        if char_eta == char_eta.lower():
            swapped_char_nu: str = char_eta.upper()
        else:
            swapped_char_nu = char_eta.lower()
        temporal_beta += swapped_char_nu
        index_mu += 1

    builder_rho: str = ""
    for char_zeta in temporal_beta:
        if char_zeta in map_theta:
            builder_rho += map_theta[char_zeta]
            continue
        builder_rho += char_zeta

    return builder_rho