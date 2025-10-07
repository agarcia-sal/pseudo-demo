from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        x1 = integer_value
        y2 = 1
        if not (x1 >= 0):
            x1 = -x1
            y2 = -y2
        z3: List[int] = []
        s4 = str(x1)
        i5 = 0
        while i5 < len(s4):
            z3.append(int(s4[i5]))
            i5 += 1
        z3[0] = z3[0] * y2
        r6 = 0
        j7 = 0
        while j7 < len(z3):
            r6 += z3[j7]
            j7 += 1
        return r6

    r8: List[int] = []
    k9 = 0
    while k9 < len(array_of_integers):
        r8.append(digits_sum(array_of_integers[k9]))
        k9 += 1
    filtered10: List[int] = []
    m11 = 0
    while m11 < len(r8):
        if r8[m11] > 0:
            filtered10.append(r8[m11])
        m11 += 1

    return len(filtered10)