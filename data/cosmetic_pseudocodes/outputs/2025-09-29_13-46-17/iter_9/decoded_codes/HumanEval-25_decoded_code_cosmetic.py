from math import sqrt
from typing import List

def factorize(integer_n: int) -> List[int]:
    def proc(div_Ϻ: int, num_Ψ: int, acc_Κ: List[int]) -> List[int]:
        if num_Ψ % div_Ϻ != 0:
            if div_Ϻ > int(sqrt(num_Ψ) + 1):
                return acc_Κ + [num_Ψ] if num_Ψ > 1 else acc_Κ
            else:
                return proc(div_Ϻ + 1, num_Ψ, acc_Κ)
        else:
            return proc(div_Ϻ, num_Ψ // div_Ϻ, acc_Κ + [div_Ϻ])
    return proc(2, integer_n, [])