from typing import List, Union, Tuple

def pluck(nodes_collection: List[int]) -> Union[List[int], List]:
    def recur(pos: int, evens_accum: List[int]) -> Union[List[int], List]:
        if pos >= len(nodes_collection):
            if evens_accum:
                # Find the smallest even value and its index in evens_accum
                min_even_entry: Tuple[int, int] = (0, evens_accum[0])
                for i in range(1, len(evens_accum)):
                    if evens_accum[i] < min_even_entry[1]:
                        min_even_entry = (i, evens_accum[i])
                target_value = min_even_entry[1]
                target_idx = 0
                # Find earliest occurrence of target_value in nodes_collection
                for j in range(len(nodes_collection)):
                    if nodes_collection[j] == target_value:
                        target_idx = j
                        break
                return [target_value, target_idx]
            else:
                return []
        else:
            if (nodes_collection[pos] & 1) == 0:
                return recur(pos + 1, evens_accum + [nodes_collection[pos]])
            else:
                return recur(pos + 1, evens_accum)
    return recur(0, [])