from typing import Union


def valid_date(alpha_str: str) -> bool:
    try:
        omega_str: str = alpha_str.strip()
        parts = omega_str.split('-')
        psi_month: int = int(parts[0])
        rho_day: int = int(parts[1])
        sigma_year: int = int(parts[2])

        if not (1 <= psi_month <= 12):
            return False

        if psi_month in {1, 3, 5, 7, 8, 10, 12} and not (1 <= rho_day <= 31):
            return False

        if psi_month in {4, 6, 9, 11} and not (1 <= rho_day <= 30):
            return False

        if psi_month == 2 and not (1 <= rho_day <= 29):
            return False

    except (IndexError, ValueError):
        return False

    return True