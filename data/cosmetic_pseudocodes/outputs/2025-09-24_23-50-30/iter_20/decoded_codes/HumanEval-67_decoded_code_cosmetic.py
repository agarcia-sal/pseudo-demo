from functools import reduce
from typing import List

def fruit_distribution(text_expression: str, aggregate_count: int) -> int:
    collection_store: List[int] = []
    elements_collection: List[str] = text_expression.split(" ")

    def index_runner(current_index: int, total_items: int) -> None:
        if current_index >= total_items:
            return
        token_item = elements_collection[current_index]
        if token_item.isdigit():
            collection_store.append(int(token_item))
        index_runner(current_index + 1, total_items)

    index_runner(0, len(elements_collection))
    return aggregate_count + (-1 * reduce(lambda accum, val: accum + val, collection_store, 0))