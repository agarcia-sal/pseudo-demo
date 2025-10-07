from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def gather_numbers(elements: List[str], acc: List[int]) -> List[int]:
        if not elements:
            return acc
        head, *tail = elements
        if head.isdigit():
            return gather_numbers(tail, acc + [int(head)])
        return gather_numbers(tail, acc)

    tokens = string_description.split(" ")
    numbers_collected = gather_numbers(tokens, [])
    sum_numbers = sum(numbers_collected)
    return total_number_of_fruits - sum_numbers