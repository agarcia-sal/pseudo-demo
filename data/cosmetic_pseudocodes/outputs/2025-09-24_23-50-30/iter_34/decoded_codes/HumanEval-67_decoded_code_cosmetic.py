from typing import List, Dict


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    bag: Dict[int, int] = {}

    def collect_numbers(lst: List[str], i: int) -> int:
        if i < len(lst):
            if lst[i].isdigit():
                val = int(lst[i])
                bag[i] = val
            return collect_numbers(lst, i + 1)
        return 0

    tokens: List[str] = string_description.split(" ")
    total_sum = sum(bag[key] for key in bag) + collect_numbers(tokens, 0)
    return total_number_of_fruits - total_sum