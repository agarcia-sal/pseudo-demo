from typing import List


def select_words(str_q: str, nat_m: int) -> List[str]:
    arr_p: List[str] = str_q.split(" ")

    def count_cons(lst_r: str, idx_t: int, ct_u: int) -> int:
        if idx_t >= len(lst_r):
            return ct_u
        ch_v: str = lst_r[idx_t].lower()
        incr_w: int = 0 if ch_v in {'a', 'e', 'i', 'o', 'u'} else 1
        return count_cons(lst_r, idx_t + 1, ct_u + incr_w)

    acc: List[str] = []
    for ele_x in arr_p:
        cons_y = count_cons(ele_x, 0, 0)
        if cons_y == nat_m:
            acc.append(ele_x)

    return acc