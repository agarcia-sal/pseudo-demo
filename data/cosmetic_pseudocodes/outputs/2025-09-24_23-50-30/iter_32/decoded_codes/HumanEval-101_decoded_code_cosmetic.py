from typing import List


def words_string(base_value: str) -> List[str]:
    if base_value == "":
        return []

    delta_array: List[str] = []

    for epsilon in base_value:
        if epsilon == ",":
            delta_array.append(" ")
        else:
            delta_array.append(epsilon)

    theta = "".join(delta_array)

    output: List[str] = []
    alpha = 0
    beta = ""

    while alpha <= len(theta):
        if alpha == len(theta) or theta[alpha] == " ":
            if beta != "":
                output.append(beta)
            beta = ""
        else:
            beta += theta[alpha]
        alpha += 1

    return output