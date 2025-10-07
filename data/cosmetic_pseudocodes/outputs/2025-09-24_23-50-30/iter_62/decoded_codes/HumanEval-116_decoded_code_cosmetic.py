from typing import List

def sort_array(param_list: List[int]) -> List[int]:
    def tally_ones(bits: str) -> int:
        def loop(idx: int, cnt: int) -> int:
            if idx < len(bits):
                return loop(idx + 1, cnt + (1 if bits[idx] == '1' else 0))
            else:
                return cnt
        return loop(0, 0)

    first_sort: List[int] = sorted(param_list)
    second_sort: List[int] = sorted(
        first_sort,
        key=lambda element: tally_ones(bin(element)[2:])
    )
    return second_sort