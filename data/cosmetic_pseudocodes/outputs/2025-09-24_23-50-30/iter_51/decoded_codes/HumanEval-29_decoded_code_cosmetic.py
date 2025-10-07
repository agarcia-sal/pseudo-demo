from typing import List

def filter_by_prefix(array_of_texts: List[str], start_pattern: str) -> List[str]:
    def accumulate_matches(
        source_collection: List[str],
        pattern: str,
        accumulator: List[str],
        index: int
    ) -> List[str]:
        if index == len(source_collection):
            return accumulator
        element = source_collection[index]
        if element.startswith(pattern):
            return accumulate_matches(source_collection, pattern, accumulator + [element], index + 1)
        return accumulate_matches(source_collection, pattern, accumulator, index + 1)

    return accumulate_matches(array_of_texts, start_pattern, [], 0)