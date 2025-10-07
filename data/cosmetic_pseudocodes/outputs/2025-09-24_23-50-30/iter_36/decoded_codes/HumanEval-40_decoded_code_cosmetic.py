from typing import Sequence


def triples_sum_to_zero(collection_numbers: Sequence[int]) -> bool:
    def check_positions(pos_a: int, pos_b: int, pos_c: int) -> bool:
        if pos_a >= len(collection_numbers) - 2:
            return False
        elif pos_b >= len(collection_numbers) - 1:
            return check_positions(pos_a + 1, pos_a + 2, pos_a + 3)
        elif pos_c >= len(collection_numbers):
            return check_positions(pos_a, pos_b + 1, pos_b + 2)
        else:
            total_sum = collection_numbers[pos_a] + collection_numbers[pos_b] + collection_numbers[pos_c]
            if total_sum == 0:
                return True
            else:
                return check_positions(pos_a, pos_b, pos_c + 1)

    return check_positions(0, 1, 2)