from typing import List

def search(collection_of_numbers: List[int]) -> int:
    max_val = max(collection_of_numbers) if collection_of_numbers else 0
    counter: List[int] = [0] * (max_val + 1)

    def recurse_count(pos: int) -> None:
        if pos >= len(collection_of_numbers):
            return
        counter[collection_of_numbers[pos]] += 1
        recurse_count(pos + 1)

    recurse_count(0)

    result: int = -1

    def find_result(iterator: int) -> None:
        nonlocal result
        if iterator > len(counter) - 1:
            return
        if counter[iterator] >= iterator:
            result = iterator
        find_result(iterator + 1)

    find_result(1)

    return result