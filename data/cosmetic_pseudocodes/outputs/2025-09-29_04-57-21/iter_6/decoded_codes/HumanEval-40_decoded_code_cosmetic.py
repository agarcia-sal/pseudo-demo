from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    def seek_triplet(current_pos: int) -> bool:
        if current_pos >= len(list_of_integers) - 2:
            return False
        for second_pos in range(current_pos + 1, len(list_of_integers) - 1):
            for third_pos in range(second_pos + 1, len(list_of_integers)):
                total_value = (
                    list_of_integers[current_pos] +
                    list_of_integers[second_pos] +
                    list_of_integers[third_pos]
                )
                if total_value == 0:
                    return True
        return seek_triplet(current_pos + 1)

    return seek_triplet(0)