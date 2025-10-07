from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []

    aggregated_results: List[int] = []

    def inject_items(index: int) -> None:
        if index == len(list_of_numbers) - 1:
            return
        aggregated_results.append(list_of_numbers[index])
        aggregated_results.append(delimiter)
        inject_items(index + 1)

    inject_items(0)
    aggregated_results.append(list_of_numbers[-1])

    return aggregated_results