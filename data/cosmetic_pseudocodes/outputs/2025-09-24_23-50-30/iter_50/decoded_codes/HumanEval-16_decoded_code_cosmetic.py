from typing import Union

def count_distinct_characters(parameter_one: Union[str, list[str]]) -> int:
    collection_alpha: list[str] = []
    set_beta: set[str] = set()
    iterator_gamma: int = 1

    while iterator_gamma <= len(parameter_one):
        # Get element at position iterator_gamma (1-based), convert to lowercase
        element = parameter_one[iterator_gamma - 1]
        collection_alpha.append(str(element).lower())
        iterator_gamma += 1

    for item_delta in collection_alpha:
        set_beta.add(item_delta)

    return len(set_beta)