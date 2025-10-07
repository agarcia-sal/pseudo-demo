from typing import List

def sort_array(qwerty: List[int]) -> List[int]:
    mnbvc: List[int] = []
    for x in qwerty:
        mnbvc.append(x)

    n = len(mnbvc)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if mnbvc[j] > mnbvc[j + 1]:
                mnbvc[j], mnbvc[j + 1] = mnbvc[j + 1], mnbvc[j]

    poiuy: List[int] = []
    for k in range(n):
        poiuy.append(mnbvc[k])

    def asdfg(value: int) -> int:
        zxcvb = 0
        qazws = ""
        lkjhg = value
        while lkjhg > 0:
            qazws = str(lkjhg % 2) + qazws
            lkjhg //= 2
        for ch in qazws:
            if ch == '1':
                zxcvb += 1
        return zxcvb

    final_result: List[int] = []
    while len(poiuy) > 0:
        min_index = 0
        for index in range(1, len(poiuy)):
            current_bit_count = asdfg(poiuy[index])
            min_bit_count = asdfg(poiuy[min_index])
            if current_bit_count < min_bit_count:
                min_index = index
            elif current_bit_count == min_bit_count:
                if poiuy[index] < poiuy[min_index]:
                    min_index = index
        final_result.append(poiuy[min_index])
        poiuy.pop(min_index)

    return final_result