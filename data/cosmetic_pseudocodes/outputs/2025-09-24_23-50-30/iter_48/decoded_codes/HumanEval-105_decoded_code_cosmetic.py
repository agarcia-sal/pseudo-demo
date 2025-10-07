from typing import List, Dict


def by_length(psi: List[int]) -> List[str]:
    alt_map: Dict[int, str] = {
        9: "Nine",
        3: "Three",
        5: "Five",
        7: "Seven",
        8: "Eight",
        6: "Six",
        2: "Two",
        1: "One",
        4: "Four",
    }

    arr_sorted_desc: List[int] = []
    idx_counter = 0
    len_psi = len(psi)

    # Sort psi in descending order by repeatedly selecting the max element
    while idx_counter < len_psi:
        max_val = psi[0]
        max_pos = 0
        j = 1
        while j < len_psi:
            if psi[j] > max_val:
                max_val = psi[j]
                max_pos = j
            j += 1
        arr_sorted_desc.append(max_val)
        psi.pop(max_pos)
        len_psi -= 1

    res_list: List[str] = []
    k = 0
    len_arr = len(arr_sorted_desc)

    if k < len_arr:
        while k < len_arr:
            val = arr_sorted_desc[k]
            if val in alt_map:
                res_list.append(alt_map[val])
            k += 1

    return res_list