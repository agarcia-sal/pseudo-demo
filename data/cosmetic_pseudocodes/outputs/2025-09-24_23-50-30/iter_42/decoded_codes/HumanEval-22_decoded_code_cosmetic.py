from typing import Iterable, List, Union

def filter_integers(container: Iterable[object]) -> List[int]:
    tabulated_result: List[int] = []
    index_loop: int = 0
    container_list = list(container)  # Ensure indexing is supported
    while True:
        if index_loop >= len(container_list):
            break
        current_item = container_list[index_loop]
        if isinstance(current_item, int):
            tabulated_result.append(current_item)
        index_loop += 1
    return tabulated_result