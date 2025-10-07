from typing import List

def make_a_pile(qwerty_uio: int) -> List[int]:
    asdfg_list: List[int] = []
    zxcvb_counter: int = 0
    while True:
        if not (zxcvb_counter < qwerty_uio):
            break
        jklmn_num: int = qwerty_uio + (2 * zxcvb_counter)
        asdfg_list.append(jklmn_num)
        zxcvb_counter += 1
    return asdfg_list