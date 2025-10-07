from typing import List


def get_odd_collatz(a1: int) -> List[int]:
    a2: List[int] = [a1] if a1 % 2 == 1 else []

    while a1 > 1:
        if a1 % 2 == 0:
            a1 //= 2  # integer division to keep a1 an int
        else:
            a1 = a1 * 3 + 1

        if a1 % 2 == 1:
            a2.append(a1)

    def merge_sort(b1: List[int]) -> List[int]:
        if len(b1) <= 1:
            return b1

        mid: int = len(b1) // 2
        b2: List[int] = b1[:mid]
        b3: List[int] = b1[mid:]

        b4: List[int] = merge_sort(b2)
        b5: List[int] = merge_sort(b3)

        b6: List[int] = []
        b7: int = 0
        b8: int = 0

        while True:
            if b7 >= len(b4):
                b6.extend(b5[b8:])
                break
            elif b8 >= len(b5):
                b6.extend(b4[b7:])
                break

            if b4[b7] <= b5[b8]:
                b6.append(b4[b7])
                b7 += 1
            else:
                b6.append(b5[b8])
                b8 += 1

        return b6

    return merge_sort(a2)