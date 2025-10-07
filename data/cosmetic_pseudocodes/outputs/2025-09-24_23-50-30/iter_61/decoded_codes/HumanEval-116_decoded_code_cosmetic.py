from typing import Sequence, List

def sort_array(data_sequence: Sequence[int]) -> List[int]:
    def count_ones_in_bin(z: int) -> int:
        v = bin(z)[2:]  # binary representation without '0b' prefix
        o = 0
        x = 0
        while x < len(v):
            if v[x] == '1':
                o += 1
            x += 1
        return o

    p = list(data_sequence)
    q = len(p)
    y = 0
    while y < q - 1:
        a = y
        z = y + 1
        while z < q:
            if p[z] < p[a]:
                a = z
            z += 1
        if a != y:
            p[y], p[a] = p[a], p[y]
        y += 1

    result_list: List[int] = []
    index = 0
    while index < q:
        count = count_ones_in_bin(p[index])
        inserted = False
        pos = 0
        while pos < len(result_list):
            c_of_pos = count_ones_in_bin(result_list[pos])
            if c_of_pos > count:
                result_list.insert(pos, p[index])
                inserted = True
                break
            pos += 1
        if not inserted:
            result_list.append(p[index])
        index += 1

    return result_list