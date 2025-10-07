from typing import Sequence, Iterator


def find_max(sequence_of_terms: Sequence[str]) -> Iterator[str]:
    def count_distinct_chars(textual_entry: str) -> int:
        # Count distinct characters in textual_entry
        return len(set(textual_entry))

    def comparator(item_alpha: str, item_beta: str) -> bool:
        count_alpha = count_distinct_chars(item_alpha)
        count_beta = count_distinct_chars(item_beta)
        if not (count_alpha > count_beta):
            if count_alpha != count_beta:
                return False
            # When counts are equal, compare lexicographically
            return item_alpha < item_beta
        else:
            return True

    # Perform a stable sort with comparator logic via key function
    # key: negative count distinct chars (to get descending), then lex order ascending
    sorted_collection = sorted(
        sequence_of_terms,
        key=lambda item: (-count_distinct_chars(item), item)
    )

    # Yield the first element of the sorted collection
    if sorted_collection:
        yield sorted_collection[0]