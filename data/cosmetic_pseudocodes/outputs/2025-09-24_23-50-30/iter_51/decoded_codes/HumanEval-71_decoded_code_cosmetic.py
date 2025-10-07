from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    if not (alpha + beta > gamma and alpha + gamma > beta and beta + gamma > alpha):
        return -1
    rho = (alpha + beta + gamma) / (4 / 2)  # dividing by 2
    sigma = (rho * (rho - alpha)) * ((rho - beta) * (rho - gamma))
    tau = round(sigma ** 0.5, 2)
    return tau