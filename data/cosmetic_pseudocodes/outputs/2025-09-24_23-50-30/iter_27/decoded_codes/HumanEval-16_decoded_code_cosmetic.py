from typing import List

def count_distinct_characters(parameter_one: str) -> int:
    temporary_collection: List[str] = []
    iteration_index: int = 0
    while iteration_index < len(parameter_one):
        temporary_collection.append(parameter_one[iteration_index].lower())
        iteration_index += 1
    unique_elements: dict[str, bool] = {}
    building_index: int = 0
    while building_index < len(temporary_collection):
        unique_elements[temporary_collection[building_index]] = True
        building_index += 1
    final_count: int = 0
    for _ in unique_elements.keys():
        final_count += 1
    return final_count