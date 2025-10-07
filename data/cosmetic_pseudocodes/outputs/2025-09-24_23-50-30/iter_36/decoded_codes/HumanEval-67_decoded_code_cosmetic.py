from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def accumulate_numbers(collection: List[str], index: int, acc: int) -> int:
        if index >= len(collection):
            return acc
        current_item = collection[index]
        next_acc = acc + int(current_item) if current_item.isdigit() else acc
        return accumulate_numbers(collection, index + 1, next_acc)

    tokens = string_description.split(" ")
    total_sum = accumulate_numbers(tokens, 0, 0)
    return total_number_of_fruits - total_sum