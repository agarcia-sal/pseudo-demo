from typing import List


def numerical_letter_grade(alpha_values: List[float]) -> List[str]:
    def epsilon_gamma_beta(delta_list: List[float], omega_list: List[str]) -> List[str]:
        if not delta_list:
            return omega_list

        def zeta_eta_theta(lambda_num: float) -> str:
            # Map numeric grade to letter grade
            if lambda_num == 4.0:
                return "A+"
            if lambda_num > 3.7:
                return "A"
            if lambda_num > 3.3:
                return "A-"
            if lambda_num > 3.0:
                return "B+"
            if lambda_num > 2.7:
                return "B"
            if lambda_num > 2.3:
                return "B-"
            if lambda_num > 2.0:
                return "C+"
            if lambda_num > 1.7:
                return "C"
            if lambda_num > 1.3:
                return "C-"
            if lambda_num > 1.0:
                return "D+"
            if lambda_num > 0.7:
                return "D"
            if lambda_num > 0.0:
                return "D-"
            return "E"

        head, *tail = delta_list
        return epsilon_gamma_beta(tail, omega_list + [zeta_eta_theta(head)])

    return epsilon_gamma_beta(alpha_values, [])