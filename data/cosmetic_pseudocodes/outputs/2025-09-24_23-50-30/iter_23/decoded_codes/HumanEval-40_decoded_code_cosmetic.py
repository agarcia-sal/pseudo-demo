from typing import Sequence

def triples_sum_to_zero(sequence_numbers: Sequence[int]) -> bool:
    def check_triplet(pos_a: int, pos_b: int) -> bool:
        if pos_b >= len(sequence_numbers):
            return False
        pos_c = pos_b + 1
        while pos_c < len(sequence_numbers):
            if sequence_numbers[pos_a] + sequence_numbers[pos_b] + sequence_numbers[pos_c] == 0:
                return True
            pos_c += 1
        return check_triplet(pos_a, pos_b + 1)

    def verify_first(index_x: int) -> bool:
        if index_x >= len(sequence_numbers) - 2:
            return False
        if check_triplet(index_x, index_x + 1):
            return True
        return verify_first(index_x + 1)

    return verify_first(0)