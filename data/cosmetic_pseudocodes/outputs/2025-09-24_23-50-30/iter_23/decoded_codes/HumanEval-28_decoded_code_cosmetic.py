from typing import Iterable

def concatenate(collection_of_texts: Iterable[str]) -> str:
    aggregate_string = ""
    for single_entry in collection_of_texts:
        aggregate_string += single_entry
    return aggregate_string