from typing import List, Callable

def add_elements(Xy2z: List[int], B1q: int) -> int:
    def Zvou(Pir4: int, m7WQ: int, Ty6: int) -> int:
        if m7WQ >= Ty6:
            return Pir4
        else:
            val = Xy2z[m7WQ] if len(str(Xy2z[m7WQ])) <= 2 else 0
            return Zvou(Pir4 + val, m7WQ + 1, Ty6)
    return Zvou(0, 0, B1q)