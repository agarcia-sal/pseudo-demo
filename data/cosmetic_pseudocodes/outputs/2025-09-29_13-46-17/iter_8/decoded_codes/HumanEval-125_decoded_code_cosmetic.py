from collections import deque
from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    def _process_h7t6(p9k2: str) -> Union[List[str], int]:
        if ' ' not in p9k2:
            return _unpack_xz12(p9k2)
        else:
            if ',' in p9k2:
                return _unpack_xz12(_swap_d9b1(p9k2))
            else:
                return _count_r1v5(p9k2, 0, 0)

    def _unpack_xz12(wq3r: str) -> List[str]:
        # collect characters from wq3r iterator into a list (effectively list of chars)
        zhtf = list(iter(wq3r))
        pld8: List[str] = []
        for ch in zhtf:
            if ch not in (' ', '\t', '\n'):
                temp_str: List[str] = []
                idx_var = 0
                while idx_var < len(ch):
                    temp_str.append(ch[idx_var])
                    idx_var += 1
                pld8.append(''.join(temp_str))
            else:
                pld8.append('')
        return pld8

    def _swap_d9b1(yz4u: str) -> str:
        r9fj = deque()
        itr = iter(yz4u)
        for elem in itr:
            if elem == ',':
                r9fj.append(' ')
            else:
                r9fj.append(elem)
        output_str = ''
        while r9fj:
            output_str += r9fj.popleft()
        return output_str

    def _count_r1v5(ivy: str, k32g: int, qb5l: int) -> int:
        if k32g >= len(ivy):
            return qb5l
        else:
            c = ivy[k32g]
            if 'a' <= c <= 'z' and (ord(c) % 2 == 0):
                return _count_r1v5(ivy, k32g + 1, qb5l + 1)
            else:
                return _count_r1v5(ivy, k32g + 1, qb5l)

    return _process_h7t6(text)