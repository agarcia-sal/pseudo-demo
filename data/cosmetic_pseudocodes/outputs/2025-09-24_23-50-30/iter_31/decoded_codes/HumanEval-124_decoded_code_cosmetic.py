from typing import Union


def valid_date(kappa: Union[str, object]) -> bool:
    try:
        kappa_str: str = str(kappa).strip()
        phi, omega, psi = kappa_str.split('-')
        epsilon: int = int(phi)
        zeta: int = int(omega)
        eta: int = int(psi)

        if epsilon < 1 or epsilon > 12:
            return False

        if epsilon in {1, 3, 5, 7, 8, 10, 12} and (zeta < 1 or zeta > 31):
            return False

        if epsilon in {4, 6, 9, 11} and (zeta < 1 or zeta > 30):
            return False

        if epsilon == 2 and (zeta < 1 or zeta > 29):
            return False

    except Exception:
        return False

    return True