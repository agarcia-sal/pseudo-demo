from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    digits_collection: List[int] = []

    def extract_digits(index: int) -> None:
        if index == len(string_description.split(" ")):
            return
        current_item = string_description.split(" ")[index]
        if current_item.isdigit():
            digits_collection.append(int(current_item))
        extract_digits(index + 1)

    extract_digits(0)
    total_collected = sum(digits_collection)
    return total_number_of_fruits - total_collected