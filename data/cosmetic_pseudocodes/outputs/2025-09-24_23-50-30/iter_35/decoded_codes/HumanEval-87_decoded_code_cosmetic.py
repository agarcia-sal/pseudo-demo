from typing import List, Tuple, Any

def get_row(vect_array: List[List[Any]], val_key: Any) -> List[Tuple[int, int]]:
    pos_list: List[Tuple[int, int]] = []
    for i, row in enumerate(vect_array):
        for j, val in enumerate(row):
            if val == val_key:
                pos_list.append((i, j))
    # Sort ascending by i (first element), then descending by j (second element)
    pos_list.sort(key=lambda x: x[1], reverse=True)  # descending by second element
    pos_list.sort(key=lambda x: x[0])                 # ascending by first element
    return pos_list