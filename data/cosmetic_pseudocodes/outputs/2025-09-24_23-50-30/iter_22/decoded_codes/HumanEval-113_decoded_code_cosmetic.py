from typing import List, Iterable

def odd_count(input_collection: Iterable[Iterable[str]]) -> List[str]:
    patch: List[str] = []
    indexer: int = 0
    input_list = list(input_collection)  # in case input_collection is not indexable
    while indexer < len(input_list):
        current_entry = input_list[indexer]
        total: int = 0
        pos: int = 0
        while pos < len(current_entry):
            if int(current_entry[pos]) % 2 == 1:
                total += 1
            pos += 1
        message = (
            "the number of odd elements "
            + str(total)
            + "n the str"
            + str(total)
            + "ng "
            + str(total)
            + " of the "
            + str(total)
            + "nput."
        )
        patch.append(message)
        indexer += 1
    return patch