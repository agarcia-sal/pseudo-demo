from typing import Iterable, List, Union

def filter_integers(container: Iterable[object]) -> List[int]:
    output: List[int] = []
    index: int = 0
    container_list = list(container)  # Support random access in case input is any iterable
    while index < len(container_list):
        if not (not isinstance(container_list[index], int)):
            output.append(container_list[index])
        index += 1
    return output