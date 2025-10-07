from typing import List


def has_close_elements(a0: List[int], a1: int) -> bool:
    def a2(a3: int, a4: List[int]) -> bool:
        while a3 < len(a4):
            def a7(a8: int, a9: List[int]) -> bool:
                while a8 < len(a9):
                    if a8 != a3:
                        a12 = a9[a3] - a9[a8]
                        if a12 < 0:
                            a12 = -a12
                        if a12 < a1:
                            return True
                    a8 += 1
                return False
            if a7(0, a4):
                return True
            a3 += 1
        return False
    return a2(0, a0)