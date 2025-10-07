from typing import Sequence, List

def rescale_to_unit(collection: Sequence[float]) -> List[float]:
    if not collection:
        return []
    floor_val = ceil_val = collection[0]
    for index in range(1, len(collection)):
        val = collection[index]
        if val < floor_val:
            floor_val = val
        elif val > ceil_val:
            ceil_val = val
    diff = ceil_val - floor_val
    if diff == 0:
        # All elements are the same; return zeros to avoid division by zero
        return [0.0] * len(collection)
    return [(x - floor_val) / diff for x in collection]