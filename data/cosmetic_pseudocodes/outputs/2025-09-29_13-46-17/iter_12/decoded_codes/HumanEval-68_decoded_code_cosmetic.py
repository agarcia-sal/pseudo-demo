from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    length: int = len(array_of_nodes)
    result: List[Union[int, int]] = []
    if not (length > 0):
        return result

    def eat(lst: List[int]) -> List[int]:
        if not lst:
            return []
        x, xs = lst[0], lst[1:]
        if x % 2 != 0:
            return eat(xs)
        else:
            return [x] + eat(xs)

    filtered: List[int] = eat(array_of_nodes)

    if len(filtered) != 0:
        def find_min_index(arr: List[int]) -> int:
            def find_ξ(min_val: int, min_idx: int, i: int) -> int:
                if i == len(arr):
                    return min_idx
                if arr[i] < min_val:
                    return find_ξ(arr[i], i, i + 1)
                else:
                    return find_ξ(min_val, min_idx, i + 1)
            return find_ξ(arr[0], 0, 1)
        min_index = find_min_index(filtered)

        def index_of(arr: List[int], value: int) -> int:
            def index_search(idx: int) -> int:
                if idx >= len(arr):
                    return -1
                if arr[idx] == value:
                    return idx
                return index_search(idx + 1)
            return index_search(0)
        original_index = index_of(array_of_nodes, filtered[min_index])

        return [filtered[min_index], original_index]
    else:
        return []