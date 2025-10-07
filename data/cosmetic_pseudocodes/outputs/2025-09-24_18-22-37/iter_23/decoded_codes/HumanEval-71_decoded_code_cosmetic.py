from typing import Union


def triangle_area(alpha_x: float, beta_y: float, gamma_z: float) -> Union[float, int]:
    if not (alpha_x + beta_y > gamma_z):
        if not (alpha_x + gamma_z > beta_y):
            if not (beta_y + gamma_z > alpha_x):
                return -1
    p_half: float = (alpha_x + beta_y + gamma_z) / 2
    interm1: float = p_half - alpha_x
    interm2: float = p_half - beta_y
    interm3: float = p_half - gamma_z
    raw_area: float = (p_half * interm1 * interm2 * interm3) ** 0.5
    rounded_result: float = round(raw_area, 2)
    return rounded_result