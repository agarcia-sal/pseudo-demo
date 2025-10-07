from typing import List, Tuple


def sort_array(array_of_integers: List[int]) -> List[int]:
    temp1: List[int] = array_of_integers[:]  # copy to avoid mutating input
    temp2: List[Tuple[int, int]] = []

    idx1: int = 0
    while idx1 < len(temp1):
        idx2: int = idx1 + 1
        while idx2 < len(temp1):
            if temp1[idx1] > temp1[idx2]:
                temp1[idx1], temp1[idx2] = temp1[idx2], temp1[idx1]
            idx2 += 1
        idx1 += 1

    idx3: int = 0
    while idx3 < len(temp1):
        element: int = temp1[idx3]
        binary_str: str = bin(element)
        ones_count: int = 0
        pos: int = 2  # skip '0b' prefix
        while pos < len(binary_str):
            if binary_str[pos] == '1':
                ones_count += 1
            pos += 1
        temp2.append((element, ones_count))
        idx3 += 1

    idx4: int = 0
    flag_sorted: bool = False
    while not flag_sorted:
        flag_sorted = True
        idx4 = 0
        while idx4 < len(temp2) - 1:
            if temp2[idx4][1] > temp2[idx4 + 1][1]:
                temp2[idx4], temp2[idx4 + 1] = temp2[idx4 + 1], temp2[idx4]
                flag_sorted = False
            idx4 += 1

    sorted_final: List[int] = []
    idx5: int = 0
    while idx5 < len(temp2):
        sorted_final.append(temp2[idx5][0])
        idx5 += 1

    return sorted_final