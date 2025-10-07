from typing import List

def odd_count(alpha: List[str]) -> List[str]:
    beta: List[str] = []

    def gamma(index: int, omega: List[str]) -> List[str]:
        if index == len(alpha):
            return omega
        else:
            sigma: int = 0
            delta: int = 0
            while delta < len(alpha[index]):
                if (ord(alpha[index][delta]) - ord('0')) % 2 != 0:
                    sigma += 1
                delta += 1
            epsilon: str = (
                "the number of odd elements " + str(sigma)
                + "n the str" + str(sigma)
                + "ng " + str(sigma)
                + " of the " + str(sigma)
                + "nput."
            )
            omega.append(epsilon)
            return gamma(index + 1, omega)

    return gamma(0, beta)