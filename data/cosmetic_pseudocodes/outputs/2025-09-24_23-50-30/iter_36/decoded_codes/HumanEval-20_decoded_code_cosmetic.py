from typing import List, Optional, Tuple

def find_closest_elements(array_data: List[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    dist_min: Optional[int] = None

    length = len(array_data)
    for i in range(length):
        for j in range(length):
            if i != j:
                diff = abs(array_data[i] - array_data[j])

                if dist_min is None:
                    dist_min = diff
                    if array_data[i] < array_data[j]:
                        pair_result = (array_data[i], array_data[j])
                    else:
                        pair_result = (array_data[j], array_data[i])
                else:
                    if diff < dist_min:
                        dist_min = diff
                        if array_data[i] < array_data[j]:
                            pair_result = (array_data[i], array_data[j])
                        else:
                            pair_result = (array_data[j], array_data[i])
    return pair_result