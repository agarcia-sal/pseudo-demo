from typing import List, Dict


def sort_third(list_input: List[int]) -> List[int]:
    list_copy: List[int] = []
    INDEX_MAP: Dict[int, int] = {}
    CUR_INDEX = 0
    FINAL_LIST: List[int] = []

    def duplicate_elements(curr_src: List[int], accum_copy: List[int], curr_idx: int) -> List[int]:
        if curr_idx == len(curr_src):
            return accum_copy
        accum_copy.append(curr_src[curr_idx])
        return duplicate_elements(curr_src, accum_copy, curr_idx + 1)

    list_copy = duplicate_elements(list_input, list_copy, 0)

    def gather_div3_elements(src_list: List[int], start_idx: int, acc_map: Dict[int, int], pos: int) -> Dict[int, int]:
        if start_idx == len(src_list):
            return acc_map
        if (start_idx % 3) == 0:
            acc_map[pos] = src_list[start_idx]
            pos_next = pos + 1
        else:
            pos_next = pos
        return gather_div3_elements(src_list, start_idx + 1, acc_map, pos_next)

    INDEX_MAP = gather_div3_elements(list_copy, 0, INDEX_MAP, 0)

    def extract_values(mapping: Dict[int, int]) -> List[int]:
        keys_list = list(mapping.keys())
        size_keys = len(keys_list)
        val_accum: List[int] = []

        def inner_extract(i: int, acc: List[int]) -> List[int]:
            if i == size_keys:
                return acc
            k = keys_list[i]
            acc.append(mapping[k])
            return inner_extract(i + 1, acc)

        return inner_extract(0, val_accum)

    VALUES_LIST = extract_values(INDEX_MAP)

    def sort_list(lst: List[int]) -> List[int]:
        if len(lst) < 2:
            return lst
        pivot = lst[0]
        lt: List[int] = []
        geq: List[int] = []

        def partition_elements(a_list: List[int], pivot_val: int, l_accum: List[int], g_accum: List[int], idx: int) -> List[List[int]]:
            if idx == len(a_list):
                return [l_accum, g_accum]
            curr_val = a_list[idx]
            if curr_val < pivot_val:
                l_accum.append(curr_val)
            else:
                g_accum.append(curr_val)
            return partition_elements(a_list, pivot_val, l_accum, g_accum, idx + 1)

        less_than, greater_equal = partition_elements(lst[1:], pivot, lt, geq, 0)
        sorted_lt = sort_list(less_than)
        sorted_geq = sort_list(greater_equal)
        return sorted_lt + [pivot] + sorted_geq

    SORTED_VALUES = sort_list(VALUES_LIST)

    def replace_div3_targets(src_list: List[int], sorted_vals_map: List[int], curr_idx: int, sorted_idx: int) -> List[int]:
        if curr_idx == len(src_list):
            return src_list
        if (curr_idx % 3) == 0:
            src_list[curr_idx] = sorted_vals_map[sorted_idx]
            return replace_div3_targets(src_list, sorted_vals_map, curr_idx + 1, sorted_idx + 1)
        else:
            return replace_div3_targets(src_list, sorted_vals_map, curr_idx + 1, sorted_idx)

    list_input = replace_div3_targets(list_copy, SORTED_VALUES, 0, 0)

    return list_input