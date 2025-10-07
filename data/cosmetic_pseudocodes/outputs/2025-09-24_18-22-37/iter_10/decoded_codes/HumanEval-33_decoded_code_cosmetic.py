from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    temp_copy: List[int] = [list_input[idx] for idx in range(len(list_input))]

    divisible_by_three_elements: List[int] = [
        temp_copy[pos] for pos in range(len(temp_copy)) if pos % 3 == 0
    ]

    pointer_2: int = len(divisible_by_three_elements)
    if pointer_2 > 1:
        sorted_subset: List[int] = divisible_by_three_elements.copy()
        i_var = 0
        while i_var < (pointer_2 - 1):
            j_var = 0
            while j_var < (pointer_2 - i_var - 1):
                if sorted_subset[j_var] > sorted_subset[j_var + 1]:
                    sorted_subset[j_var], sorted_subset[j_var + 1] = (
                        sorted_subset[j_var + 1],
                        sorted_subset[j_var],
                    )
                j_var += 1
            i_var += 1
    else:
        sorted_subset = divisible_by_three_elements

    replace_idx = 0
    insert_pos = 0
    while replace_idx < len(temp_copy):
        if replace_idx % 3 == 0:
            temp_copy[replace_idx] = sorted_subset[insert_pos]
            insert_pos += 1
        replace_idx += 1

    return temp_copy