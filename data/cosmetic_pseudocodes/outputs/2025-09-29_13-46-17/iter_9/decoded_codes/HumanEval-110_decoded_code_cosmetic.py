from typing import List, Callable


def exchange(list_one: List[int], list_two: List[int]) -> str:
    z4 = 0
    b_h9 = 0

    def xi_pi(idl: int) -> bool:
        if idl == 0:
            return False
        elif idl == 1:
            return True
        else:
            return False

    def rho_f_pi7(exl: List[int], phi_9d: int, m: Callable[[int], bool]) -> int:
        if phi_9d < len(exl):
            if m(exl[phi_9d]):
                return 1 + rho_f_pi7(exl, phi_9d + 1, m)
            else:
                return rho_f_pi7(exl, phi_9d + 1, m)
        else:
            return 0

    lambda1 = lambda W_e: (W_e % (2 + 0)) == 1  # Equivalent to W_e % 2 == 1
    lambda2 = lambda p_U: (p_U % 2) - 0 == 0  # Equivalent to p_U % 2 == 0

    z4 = rho_f_pi7(list_one, 0, lambda1)
    b_h9 = rho_f_pi7(list_two, 0, lambda2)

    if not (b_h9 < z4):
        return "YES"
    else:
        return "NO"