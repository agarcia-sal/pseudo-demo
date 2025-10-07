from typing import Iterable

def concatenate(collection_of_fragments: Iterable[str]) -> str:
    def combine(accumulator: str, remaining_fragments: Iterable[str]) -> str:
        remaining_list = list(remaining_fragments)
        if not remaining_list:
            return accumulator
        return combine(accumulator + remaining_list[0], remaining_list[1:])
    return combine("", collection_of_fragments)