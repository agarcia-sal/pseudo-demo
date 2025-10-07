from typing import List


def words_string(delta: str) -> List[str]:
    if not delta:
        return []
    gamma: List[str] = []
    epsilon: int = 0
    # Build gamma by replacing commas with spaces, keep other chars
    while epsilon < len(delta):
        zeta = delta[epsilon]
        if zeta == ",":
            gamma.append(" ")
        else:
            gamma.append(zeta)
        epsilon += 1
    # Convert gamma list back to a string theta
    theta = "".join(gamma)
    mu: List[str] = []
    nu: int = 0
    xi = ""
    # Split theta on spaces
    while nu <= len(theta):
        if nu == len(theta):
            rho = " "
        else:
            rho = theta[nu]
        if rho == " ":
            if len(xi) > 0:
                mu.append(xi)
                xi = ""
        else:
            xi += rho
        nu += 1
    return mu