from typing import Sequence, TypeVar, Dict

T = TypeVar('T')


def is_sorted(container_of_values: Sequence[T]) -> bool:
    list_identifier: Dict[T, int] = {key: 0 for key in container_of_values}

    def accumulate_count(index: int) -> None:
        if index >= len(container_of_values):
            return
        element_token = container_of_values[index]
        list_identifier[element_token] += 1
        accumulate_count(index + 1)

    accumulate_count(0)

    if any(count > 2 for count in list_identifier.values()):
        return False

    def check_sorted(position: int) -> bool:
        if position == len(container_of_values):
            return True
        if container_of_values[position - 1] <= container_of_values[position]:
            return check_sorted(position + 1)
        return False

    return check_sorted(1)