from typing import List, Dict


def by_length(original_list: List[int]) -> List[str]:
    lookup_map: Dict[int, str] = {
        9: "Nine",
        7: "Seven",
        8: "Eight",
        3: "Three",
        6: "Six",
        1: "One",
        4: "Four",
        2: "Two",
        5: "Five",
    }
    descending_list: List[int] = []
    index_key: int = 0  # defined but unused per pseudocode

    def build_descending(input_collection: List[int], result_collection: List[int]) -> List[int]:
        if not input_collection:
            return result_collection
        max_value: int = input_collection[0]
        for item in input_collection:
            if item > max_value:
                max_value = item
        result_collection.append(max_value)
        filtered_collection = [num for num in input_collection if num != max_value]
        return build_descending(filtered_collection, result_collection)

    descending_list = build_descending(original_list, descending_list)

    def translate_elements(collection_to_translate: List[int], accumulated_result: List[str]) -> List[str]:
        if not collection_to_translate:
            return accumulated_result
        current_element = collection_to_translate[0]
        tail_collection = collection_to_translate[1:]
        if current_element in lookup_map:
            updated_result = accumulated_result + [lookup_map[current_element]]
        else:
            updated_result = accumulated_result
        return translate_elements(tail_collection, updated_result)

    return translate_elements(descending_list, [])