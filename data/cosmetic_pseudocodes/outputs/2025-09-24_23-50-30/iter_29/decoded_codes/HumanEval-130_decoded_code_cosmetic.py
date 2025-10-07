from typing import List


def tri(x: int) -> List[int]:
    match x:
        case 0:
            return [1]
        case _:
            p: List[int] = [1, 3]

            def f(i: int, arr: List[int]) -> List[int]:
                if i > x:
                    return arr
                if i % 2 == 0:
                    val = (i // 2) + 1  # integer division as index-based
                else:
                    val = arr[i - 1] + arr[i - 2] + ((i + 3) // 2)
                return f(i + 1, arr + [val])

            return f(2, p)