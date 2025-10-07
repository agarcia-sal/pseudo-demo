from typing import List

def derivative(array_of_terms: List[int]) -> List[int]:
    def process_at_index(array_of_terms: List[int], integer_index: int) -> int:
        return integer_index * array_of_terms[integer_index]

    def build_result(integer_count: int) -> List[int]:
        def iterate_accum(integer_current: int, integer_limit: int, list_accumulator: List[int]) -> List[int]:
            if integer_current > integer_limit:
                return list_accumulator
            else:
                return iterate_accum(integer_current + 1, integer_limit, list_accumulator + [process_at_index(array_of_terms, integer_current)])
        return iterate_accum(1, integer_count - 1, [])

    return build_result(len(array_of_terms))