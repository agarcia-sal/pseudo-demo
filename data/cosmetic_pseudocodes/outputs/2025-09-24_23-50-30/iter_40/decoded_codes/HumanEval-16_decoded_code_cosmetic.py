from typing import Iterable

def count_distinct_characters(data: Iterable[str]) -> int:
    collection = [item.lower() for item in data]
    unique_items = {}
    index = 0
    while index < len(collection):
        unique_items[collection[index]] = True
        index += 1
    return len(unique_items)