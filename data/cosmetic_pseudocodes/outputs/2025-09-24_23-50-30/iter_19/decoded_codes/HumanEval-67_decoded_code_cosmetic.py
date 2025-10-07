from typing import List


def fruit_distribution(input_string: str, total_fruits: int) -> int:
    nums_collection: List[int] = []
    split_tokens: List[str] = input_string.split(" ")
    for token in split_tokens:
        if token.isdigit():
            nums_collection.append(int(token))
    total_extracted: int = sum(nums_collection)
    return total_fruits - total_extracted