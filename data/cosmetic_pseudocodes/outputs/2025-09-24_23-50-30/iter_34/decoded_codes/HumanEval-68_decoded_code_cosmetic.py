from typing import List, Optional, Union

def pluck(qr: List[int]) -> Union[List[int], List]:
    def recursively_filter(p: List[int], acc: List[int]) -> List[int]:
        if not p:
            return acc
        head_element = p[0]
        tail_elements = p[1:]
        if head_element % 2 == 0:
            return recursively_filter(tail_elements, acc + [head_element])
        else:
            return recursively_filter(tail_elements, acc)

    def find_minimum(lst: List[int]) -> Optional[int]:
        def helper(i: int, curr_min: int) -> int:
            if i == len(lst):
                return curr_min
            val = lst[i]
            if val < curr_min:
                return helper(i + 1, val)
            else:
                return helper(i + 1, curr_min)

        if not lst:
            return None
        return helper(1, lst[0])

    def find_index(lst: List[int], val: int, idx: int) -> int:
        if idx == len(lst):
            return -1
        if lst[idx] == val:
            return idx
        else:
            return find_index(lst, val, idx + 1)

    if len(qr) != 0:
        filtered = recursively_filter(qr, [])
        if len(filtered) != 0:
            minimal = find_minimum(filtered)
            # minimal is Optional[int], but filtered non-empty means minimal not None
            position = find_index(qr, minimal, 0)  # type: ignore
            return [minimal, position]  # type: ignore

    return []