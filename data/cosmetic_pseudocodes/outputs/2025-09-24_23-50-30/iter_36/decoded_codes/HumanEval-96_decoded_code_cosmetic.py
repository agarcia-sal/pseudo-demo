from typing import List

def count_up_to(b: int) -> List[int]:
    arr: List[int] = []

    def check_prime(x: int, y: int) -> bool:
        if y * y > x:
            return True
        if x % y == 0:
            return False
        return check_prime(x, y + 1)

    def gather(c: int) -> List[int]:
        if c >= b:
            return arr
        if check_prime(c, 2):
            arr.append(c)
        return gather(c + 1)

    return gather(2)