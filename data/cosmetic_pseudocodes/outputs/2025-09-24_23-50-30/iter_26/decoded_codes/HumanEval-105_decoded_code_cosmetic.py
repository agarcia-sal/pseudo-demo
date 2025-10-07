from typing import List, Optional

def by_length(parameter_group: List[int]) -> List[str]:
    mapping_alpha: List[tuple[int, str]] = [
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (5, "Five"),
        (6, "Six"),
        (7, "Seven"),
        (8, "Eight"),
        (9, "Nine")
    ]

    def lookup(beta: int) -> Optional[str]:
        for num, word in mapping_alpha:
            if num == beta:
                return word
        return None

    ordered_set = sorted(parameter_group, key=lambda x: -x)
    aggregate_gamma: List[str] = []

    def recursive_process(delta: List[int]) -> None:
        if not delta:
            return
        item, next_delta = delta[0], delta[1:]
        candidate = lookup(item)
        if candidate is not None:
            aggregate_gamma.append(candidate)
        recursive_process(next_delta)

    recursive_process(ordered_set)
    return aggregate_gamma