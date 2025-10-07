from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    def check_triplets(current_pos: int) -> bool:
        if current_pos >= len(list_of_integers) - 2:
            return False

        def search_second_level(second_pos: int) -> bool:
            if second_pos >= len(list_of_integers) - 1:
                return check_triplets(current_pos + 1)

            def search_third_level(third_pos: int) -> bool:
                if third_pos >= len(list_of_integers):
                    return search_second_level(second_pos + 1)

                sum_values = (
                    list_of_integers[current_pos]
                    + list_of_integers[second_pos]
                    + list_of_integers[third_pos]
                )

                if sum_values == 0:
                    return True
                return search_third_level(third_pos + 1)

            return search_third_level(second_pos + 1)

        return search_second_level(current_pos + 1)

    return check_triplets(0)