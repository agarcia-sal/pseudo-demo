from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    def convert(ξ: List[int]) -> List[int]:
        if not ξ:
            return []
        head, tail = ξ[0], ξ[1:]
        filtered_tail = convert(tail)
        if head <= 0:
            return filtered_tail
        else:
            return [head] + filtered_tail
    return convert(list_of_numbers)