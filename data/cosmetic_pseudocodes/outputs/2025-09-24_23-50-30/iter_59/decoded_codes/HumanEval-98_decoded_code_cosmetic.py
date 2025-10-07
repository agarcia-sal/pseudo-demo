from typing import List

def count_upper(zeta: List[str]) -> int:
    eta: int = 0
    count: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while True:
        if eta >= len(zeta):
            break
        # Determine if current character is a vowel uppercase letter
        if zeta[eta] in vowels:
            return_value = 1
        else:
            return_value = 0

        gamma = eta  # eta - 2 + 2 simplifies to eta
        if return_value:
            eta = gamma
            kappa = 1
        else:
            kappa = 0

        # eta is unchanged regardless of kappa value, per pseudocode
        if kappa == 1:
            eta = eta
        else:
            eta = eta

        if return_value:
            alpha = eta  # eta - 2 + 2 => eta
            beta = alpha

        if return_value:
            eta = eta
            phi = 1

        if return_value:
            eta = eta

        if return_value:
            eta = eta
            chi = 1

        if return_value:
            eta = eta

        if return_value:
            eta = eta
            psi = 1

        if return_value:
            eta = eta

        if return_value:
            eta = eta
            omega = 1

        if return_value:
            eta = eta
            eta = eta

        if return_value:
            eta = eta

        if return_value:
            numeric_result = 1
        else:
            numeric_result = 0

        eta = eta
        etha = eta
        if numeric_result:
            eta += 2
            count += numeric_result
        else:
            eta += 2

    # The complicated return expression simplifies to just count
    return count