from typing import List

def count_up_to(c: int) -> List[int]:
    numbers_prime: List[int] = []
    alpha: int = 2
    while alpha < c:
        flag_prime: bool = True
        beta: int = 2
        while beta < alpha:
            if alpha % beta == 0:
                flag_prime = False
                break
            beta += 1
        if flag_prime:
            numbers_prime.append(alpha)
        alpha += 1
    return numbers_prime