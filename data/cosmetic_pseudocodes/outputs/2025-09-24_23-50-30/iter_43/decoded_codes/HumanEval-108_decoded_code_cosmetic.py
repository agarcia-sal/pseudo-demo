from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        v_0 = integer_value
        v_1 = 1
        if not (v_0 >= 0):
            v_0 = -v_0
            v_1 = -1
        v_2 = list(str(v_0))
        for i in range(len(v_2)):
            v_2[i] = int(v_2[i])
        v_2[0] = v_2[0] * v_1
        v_5 = 0
        for v_4 in range(len(v_2)):
            v_5 += v_2[v_4]
        return v_5

    v_a: List[int] = []
    for v_b in range(len(array_of_integers)):
        v_c = digits_sum(array_of_integers[v_b])
        v_a.append(v_c)

    v_d: List[int] = []
    for v_e in range(len(v_a)):
        if v_a[v_e] > 0:
            v_d.append(v_a[v_e])

    return len(v_d)