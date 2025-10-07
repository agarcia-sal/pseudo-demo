from typing import List


def fruit_distribution(text_data: str, total: int) -> int:
    counter: int = 0
    collection: List[int] = []
    tokens: List[str] = text_data.split(" ")
    while counter < len(tokens):
        candidate = tokens[counter]
        if candidate.isdigit():
            collection.append(int(candidate))
        counter += 1
    aggregate: int = 0
    for item in collection:
        aggregate += item
    return total - aggregate