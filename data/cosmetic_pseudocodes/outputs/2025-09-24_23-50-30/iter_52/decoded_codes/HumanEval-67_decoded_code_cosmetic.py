from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def accumulate_numbers(collection: List[str], accumulator: int) -> int:
        if not collection:
            return accumulator
        head, tail = collection[0], collection[1:]
        if head.isdigit():
            return accumulate_numbers(tail, accumulator + int(head))
        return accumulate_numbers(tail, accumulator)

    elements = string_description.split(" ")
    total_of_matches = accumulate_numbers(elements, 0)
    return total_number_of_fruits - total_of_matches