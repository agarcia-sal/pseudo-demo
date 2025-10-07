from typing import List, Any


def find_max(nominal_collection: List[Any]) -> Any:
    total_entries: int = len(nominal_collection)

    def recursive_order(position: int) -> None:
        if position < total_entries - 1:
            current_item = nominal_collection[position]
            next_item = nominal_collection[position + 1]
            unique_count_current = len(set(current_item.CHARACTERS))
            unique_count_next = len(set(next_item.CHARACTERS))
            if (unique_count_current < unique_count_next) or (
                unique_count_current == unique_count_next and current_item > next_item
            ):
                nominal_collection[position], nominal_collection[position + 1] = (
                    nominal_collection[position + 1],
                    nominal_collection[position],
                )
                recursive_order(0)
            else:
                recursive_order(position + 1)

    recursive_order(0)
    return nominal_collection[0]