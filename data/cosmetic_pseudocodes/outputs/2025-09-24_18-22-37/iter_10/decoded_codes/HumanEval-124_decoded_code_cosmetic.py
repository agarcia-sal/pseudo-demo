from typing import Optional


def valid_date(alpha_string: str) -> bool:
    try:
        omega_string: str = alpha_string.strip()
        gamma_list: list[str] = omega_string.split('-')
        if len(gamma_list) != 3:
            return False

        phi_month_string, psi_day_string, chi_year_string = gamma_list

        tau_month: int = int(phi_month_string)
        sigma_day: int = int(psi_day_string)
        _rho_year: int = int(chi_year_string)  # year is parsed but unused for validation

        if tau_month < 1 or tau_month > 12:
            return False

        if tau_month in {1, 3, 5, 7, 8, 10, 12}:
            if sigma_day < 1 or sigma_day > 31:
                return False
        elif tau_month in {4, 6, 9, 11}:
            if sigma_day < 1 or sigma_day > 30:
                return False
        elif tau_month == 2:
            if sigma_day < 1 or sigma_day > 29:
                return False
        else:
            return False  # Defensive fallback, though all months covered

    except Exception:
        return False

    return True