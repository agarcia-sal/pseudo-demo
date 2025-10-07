from typing import List


def move_one_ball(input_list: List[int]) -> bool:
    if not input_list:
        return True

    ordered_list = sorted(input_list)
    min_element = min(input_list)
    pos = input_list.index(min_element)

    # The pseudocode slices from pos to end, then from start to pos-1, concatenated
    rearranged_list = input_list[pos:] + input_list[:pos]

    def check_match(iterator_a: int, iterator_b: int) -> bool:
        while iterator_a < len(ordered_list):
            if rearranged_list[iterator_a] != ordered_list[iterator_b]:
                return False
            iterator_a += 1
            iterator_b += 1
        return True

    return check_match(0, 0)