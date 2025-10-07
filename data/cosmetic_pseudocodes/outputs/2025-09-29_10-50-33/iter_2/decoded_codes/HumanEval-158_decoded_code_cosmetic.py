from typing import Iterable, Iterator

def find_max(words_collection: Iterable[str]) -> Iterator[str]:
    # Sort by descending count of unique characters, then ascending alphabetically
    sorted_result = sorted(
        words_collection,
        key=lambda word: (-len(set(word)), word)
    )
    if sorted_result:
        yield sorted_result[0]