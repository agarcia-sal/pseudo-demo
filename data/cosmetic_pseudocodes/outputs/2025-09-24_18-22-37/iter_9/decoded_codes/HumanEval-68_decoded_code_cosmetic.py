from typing import List, Union


def pluck(nodes_collection: List[int]) -> List[Union[int, int]]:
    result_collection: List[Union[int, int]] = []

    if len(nodes_collection) != 0:
        temporary_even_collection: List[int] = [
            node for node in nodes_collection if node % 2 == 0
        ]

        if len(temporary_even_collection) != 0:
            current_minimum = temporary_even_collection[0]
            minimum_position = 1  # 1-based index per pseudocode
            iterator = 1

            while iterator <= len(temporary_even_collection):
                if temporary_even_collection[iterator - 1] < current_minimum:
                    current_minimum = temporary_even_collection[iterator - 1]
                    minimum_position = iterator
                iterator += 1

            final_index = 1
            search_index = 1
            while search_index <= len(nodes_collection):
                if nodes_collection[search_index - 1] == current_minimum:
                    final_index = search_index
                    break
                search_index += 1

            result_collection.append(current_minimum)
            result_collection.append(final_index)

            return result_collection
        else:
            return result_collection
    else:
        return result_collection