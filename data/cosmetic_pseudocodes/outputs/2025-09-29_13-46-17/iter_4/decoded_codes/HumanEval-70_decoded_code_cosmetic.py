from typing import List, Dict

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    aggregated_result: List[int] = []

    def recursive_process(collection_map: Dict[int, int], toggle_flag: bool) -> None:
        if not collection_map:
            return
        selected_element = min(collection_map.values()) if toggle_flag else max(collection_map.values())
        aggregated_result.append(selected_element)
        # Remove the key corresponding to the selected_element
        for key, value in collection_map.items():
            if value == selected_element:
                del collection_map[key]
                break
        recursive_process(collection_map, not toggle_flag)

    element_map = {i: val for i, val in enumerate(list_of_integers)}
    recursive_process(element_map, True)
    return aggregated_result