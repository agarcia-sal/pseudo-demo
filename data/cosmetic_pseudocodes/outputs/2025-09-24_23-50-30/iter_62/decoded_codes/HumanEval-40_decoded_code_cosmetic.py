from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def search_triplet(position_a: int) -> bool:
        if position_a >= len(sequence_of_numbers) - 2:
            return False

        def search_second(position_b: int) -> bool:
            if position_b >= len(sequence_of_numbers) - 1:
                return False

            def search_third(position_c: int) -> bool:
                if position_c >= len(sequence_of_numbers):
                    return False
                if (
                    sequence_of_numbers[position_a]
                    + sequence_of_numbers[position_b]
                    + sequence_of_numbers[position_c]
                    == 0
                ):
                    return True
                else:
                    return search_third(position_c + 1)

            if search_third(position_b + 1):
                return True
            else:
                return search_second(position_b + 1)

        if search_second(position_a + 1):
            return True
        else:
            return search_triplet(position_a + 1)

    return search_triplet(0)