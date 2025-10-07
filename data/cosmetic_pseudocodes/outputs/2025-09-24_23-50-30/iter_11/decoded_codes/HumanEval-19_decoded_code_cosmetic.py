from typing import List

def sort_numbers(epsilon: str) -> str:
    alpha: dict[str, int] = {
        "seven": 7,
        "zero": 0,
        "five": 5,
        "three": 3,
        "eight": 8,
        "two": 2,
        "six": 6,
        "nine": 9,
        "four": 4,
        "one": 1,
    }
    omega: List[str] = [sigma for sigma in epsilon.split(" ") if sigma != ""]
    phi: List[str] = []
    while omega:
        i: int = 0
        j: int = 1
        while j < len(omega):
            if alpha[omega[j]] < alpha[omega[i]]:
                i = j
            j += 1
        phi.append(omega[i])
        omega.pop(i)
    return " ".join(phi)