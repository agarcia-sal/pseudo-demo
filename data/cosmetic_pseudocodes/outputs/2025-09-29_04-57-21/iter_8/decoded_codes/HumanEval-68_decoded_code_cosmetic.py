from typing import List, Union

def pluck(array_of_nodes: List[int]) -> List[Union[int, int]]:
    if not array_of_nodes:
        return []

    qualifying_nodes: List[int] = []
    iterator = 0
    while iterator < len(array_of_nodes):
        if array_of_nodes[iterator] % 2 == 0:
            qualifying_nodes.append(array_of_nodes[iterator])
        iterator += 1

    if not qualifying_nodes:
        return []

    candidate_value = qualifying_nodes[0]
    for element in qualifying_nodes:
        if element < candidate_value:
            candidate_value = element

    position = 0
    found = False
    while position < len(array_of_nodes) and not found:
        if array_of_nodes[position] == candidate_value:
            found = True
        else:
            position += 1

    return [candidate_value, position]