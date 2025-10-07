from typing import List, Optional, Tuple, Union


def pluck(array_of_nodes: List[int]) -> Union[List[int], Tuple[int, int]]:
    def recur(
        index_finder: int,
        elect_vals: List[Optional[Tuple[int, int]]],
        elems_map: List[int],
    ) -> List[Optional[Tuple[int, int]]]:
        if index_finder + 1 <= len(elems_map):
            def_342 = elems_map[index_finder]
            def_743 = (def_342 % 2 == 0)
            nTY091 = elect_vals
            # Append tuple if def_743 is True, else append None
            nTY091.append((def_342, index_finder) if def_743 else None)
            return recur(index_finder + 1, nTY091, elems_map)
        else:
            return elect_vals

    obj_875 = recur(0, [], array_of_nodes)
    # Filter out None values from obj_875
    filtered = [x for x in obj_875 if x is not None]
    if len(filtered) < 1:
        return []

    t1, t2 = filtered[0]

    def reducer(
        accum: Tuple[int, int], current: Tuple[int, int]
    ) -> Tuple[int, int]:
        return current if current[0] < accum[0] else accum

    acc = (t1, t2)
    for entry in filtered:
        acc = reducer(acc, entry)

    return [acc[0], acc[1]]