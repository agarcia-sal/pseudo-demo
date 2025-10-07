from typing import List, Dict


def maximum(array_of_integers: List[int], positive_integer_k: int) -> Dict[int, int]:
    def _extract_highest_values(randomSet: List[int], K_val: int, setLength: int) -> Dict[int, int]:
        if not (K_val > 0):
            return {}

        sorted_seq = _sort_asc(randomSet, 0, setLength - 1)
        return _slice_tail(sorted_seq, setLength, K_val)

    def _sort_asc(sequence: List[int], startIndex: int, endIndex: int) -> List[int]:
        if startIndex >= endIndex:
            return sequence

        pivotIndex = _partition(sequence, startIndex, endIndex)
        sequence = _sort_asc(sequence, startIndex, pivotIndex - 1)
        sequence = _sort_asc(sequence, pivotIndex + 1, endIndex)
        return sequence

    def _partition(arr: List[int], low: int, high: int) -> int:
        pivot_element = arr[high]
        divider = low - 1
        for idx in range(low, high):
            if arr[idx] <= pivot_element:
                divider += 1
                _swap(arr, divider, idx)
        _swap(arr, divider + 1, high)
        return divider + 1

    def _swap(container: List[int], i: int, j: int) -> None:
        container[i], container[j] = container[j], container[i]

    def _slice_tail(seq: List[int], totalLen: int, itemsCount: int) -> Dict[int, int]:
        result_builder: Dict[int, int] = {}

        def recursor(index: int, startIdx: int) -> None:
            if index == itemsCount:
                return
            result_builder[index] = seq[startIdx + index]
            recursor(index + 1, startIdx)

        recursor(0, totalLen - itemsCount)
        return result_builder

    return _extract_highest_values(array_of_integers, positive_integer_k, len(array_of_integers))