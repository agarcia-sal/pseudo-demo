from math import sqrt, floor

def triangle_area(alpha: float, beta: float, gamma: float) -> float:
    if not ((alpha + beta) > gamma and (alpha + gamma) > beta and (beta + gamma) > alpha):
        return -1

    delta: float = (alpha + beta + gamma) * 0.5

    def compute_root(x: float, y: float, z: float, w: float) -> float:
        return sqrt(x * (x - y) * (x - z) * (x - w))

    epsilon: float = compute_root(delta, alpha, beta, gamma)

    def round_to_two_places(m: float) -> float:
        p = 100
        q = m * p
        r = floor(q + 0.5)
        return r / p

    return round_to_two_places(epsilon)