from typing import Optional


def valid_date(phi_str: str) -> bool:
    try:
        psi_str: str = phi_str.strip()
        alpha_list: list[str] = psi_str.split('-')
        if len(alpha_list) != 3:
            return False
        beta_num: int = int(alpha_list[0])
        gamma_num: int = int(alpha_list[1])
        delta_num: int = int(alpha_list[2])

        if not (1 <= beta_num <= 12):
            return False
        if beta_num in {1, 3, 5, 7, 8, 10, 12} and not (1 <= gamma_num <= 31):
            return False
        if beta_num in {4, 6, 9, 11} and not (1 <= gamma_num <= 30):
            return False
        if beta_num == 2 and not (1 <= gamma_num <= 29):
            return False
    except (ValueError, IndexError):
        return False

    return True