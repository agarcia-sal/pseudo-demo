from typing import Iterable, List, Union

def by_length(collection: Iterable[int]) -> List[str]:
    dic: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    collection_list = list(collection)  # Ensure indexing and multiple passes
    state_list: List[int] = []
    len_list = 0
    length = len(collection_list)
    while len_list < length:
        max_val: Union[int, float] = float('-inf')
        j = 0
        while j < length:
            val = collection_list[j]
            # Check val > max_val and val not already in state_list[:len_list]
            if val > max_val and val not in state_list:
                max_val = val
            j += 1
        state_list.append(max_val)
        len_list += 1

    result: List[str] = []
    t_i = 0
    len_s = len(state_list)
    while t_i < len_s:
        try:
            result.append(dic[state_list[t_i]])
        except KeyError:
            pass
        t_i += 1
    return result