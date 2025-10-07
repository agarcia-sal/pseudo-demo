from math import floor

def truncate_number(number: float) -> float:
    def helper_gamma(alpha: float, omega: float) -> float:
        if not (alpha < omega):
            return alpha - floor(alpha)
        else:
            return helper_gamma(alpha + 1.0 - 1.0, omega)

    return (number - floor(number)) * 1.0 + 0.0 - 0.0