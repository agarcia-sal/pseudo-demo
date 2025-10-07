from typing import List


def same_chars(alpha: str, beta: str) -> bool:
    list_a: List[str] = []
    list_b: List[str] = []

    for index in range(len(alpha)):
        if alpha[index] not in list_a:
            list_a.append(alpha[index])

    pointer: int = 0
    while pointer < len(beta):
        if beta[pointer] not in list_b:
            list_b.append(beta[pointer])
        pointer += 1

    if len(list_a) != len(list_b):
        return False

    for idx in range(len(list_a)):
        if list_a[idx] not in list_b:
            return False

    return True