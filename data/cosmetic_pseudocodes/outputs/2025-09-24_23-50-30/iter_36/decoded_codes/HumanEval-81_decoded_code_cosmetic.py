from typing import List

def numerical_letter_grade(alpha_values: List[float]) -> List[str]:
    def helper(beta_values: List[float], gamma_results: List[str]) -> List[str]:
        if not beta_values:
            return gamma_results
        delta = beta_values[0]
        epsilon = beta_values[1:]
        if delta == 4.0:
            zeta = "A+"
        elif delta > 3.7:
            zeta = "A"
        elif delta > 3.3:
            zeta = "A-"
        elif delta > 3.0:
            zeta = "B+"
        elif delta > 2.7:
            zeta = "B"
        elif delta > 2.3:
            zeta = "B-"
        elif delta > 2.0:
            zeta = "C+"
        elif delta > 1.7:
            zeta = "C"
        elif delta > 1.3:
            zeta = "C-"
        elif delta > 1.0:
            zeta = "D+"
        elif delta > 0.7:
            zeta = "D"
        elif delta > 0.0:
            zeta = "D-"
        else:
            zeta = "E"
        return helper(epsilon, gamma_results + [zeta])
    return helper(alpha_values, [])