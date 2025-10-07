from typing import List

def generate_integers(number_one: int, number_two: int) -> List[int]:
    start_limit: int = min(number_one, number_two)
    if start_limit < 2:
        start_limit = 2

    end_limit: int = max(number_one, number_two)
    if end_limit > 8:
        end_limit = 8

    even_numbers_collection: List[int] = []
    current_value: int = start_limit

    while current_value <= end_limit:
        if current_value % 2 == 0:
            even_numbers_collection.append(current_value)
        current_value += 1

    return even_numbers_collection