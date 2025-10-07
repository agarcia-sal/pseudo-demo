from typing import List, Union


class NodeCollection:
    def length(self) -> int:
        ...

    def at(self, index: int) -> int:
        ...


def pluck(node_collection: NodeCollection) -> Union[List[int], List]:
    if node_collection.length() != 0:
        filtered_evens: List[int] = []
        i: int = 0
        while i < node_collection.length():
            val: int = node_collection.at(i)
            if val % 2 == 0:
                filtered_evens.append(val)
            i += 1

        if len(filtered_evens) == 0:
            return []
        else:
            min_even_val: int = filtered_evens[0]
            i = 1
            while i < len(filtered_evens):
                if filtered_evens[i] < min_even_val:
                    min_even_val = filtered_evens[i]
                i += 1

            min_even_pos: int = -1
            i = 0
            while i < node_collection.length():
                val = node_collection.at(i)
                if val == min_even_val:
                    min_even_pos = i
                    return [min_even_val, min_even_pos]
                i += 1
    else:
        return []