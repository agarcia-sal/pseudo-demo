from typing import List


def tri(cipher: int) -> List[int]:
    t: List[int] = [1]
    if cipher != 0:
        t = [1, 3]
        index = 2
        while index <= cipher:
            modular = index % 2
            if modular == 0:
                t.append(index // 2 + 1)
            else:
                t.append(t[index - 1] + t[index - 2] + (index + 3) // 2)
            index += 1
    return t