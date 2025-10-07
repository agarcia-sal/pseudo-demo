from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def helper(queue: List[str], collection: List[int]) -> List[int]:
        if not queue:
            return collection
        head, *tail = queue
        if head.isdigit():
            updated_collection = collection + [int(head)]
        else:
            updated_collection = collection
        return helper(tail, updated_collection)

    tokens = string_description.split(" ")
    numbers_list = helper(tokens, [])
    total_sum = sum(numbers_list)
    return total_number_of_fruits - total_sum