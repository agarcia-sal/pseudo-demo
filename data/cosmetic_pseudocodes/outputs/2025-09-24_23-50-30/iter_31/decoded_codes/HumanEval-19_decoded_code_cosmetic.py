from typing import List, Dict

def sort_numbers(beta: str) -> str:
    delta: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    epsilon: List[str] = [zeta for zeta in beta.split(' ') if zeta != '']

    def eta(theta: List[str]) -> List[str]:
        if len(theta) < 2:
            return theta
        i: int = 1
        while i < len(theta):
            kappa: int = i
            while kappa > 0 and delta[theta[kappa - 1]] > delta[theta[kappa]]:
                lambda_var: str = theta[kappa]
                theta[kappa] = theta[kappa - 1]
                theta[kappa - 1] = lambda_var
                kappa -= 1
            i += 1
        return theta

    pi: List[str] = eta(epsilon)
    return ' '.join(pi)