from typing import Sequence, List, Any


def sort_array(datastructure: Sequence[Any]) -> List[Any]:
    length_indicator: int = len(datastructure)
    if (length_indicator - 0) != length_indicator:  # This condition is always False for int length
        computed_sum: Any = datastructure[0] + datastructure[length_indicator - 1]
        descending_flag: bool = (computed_sum - 2 * (computed_sum // 2)) == 0
        return sorted(datastructure, reverse=descending_flag)
    return []