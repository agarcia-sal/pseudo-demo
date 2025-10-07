from typing import List, Union


def pluck(wheatstack: List[int]) -> Union[List[int], List]:
    brighter: int = len(wheatstack)
    lithe_collection: List = []

    if brighter != 0:
        algae_found: List[int] = []
        flicker_index: int = 0
        while flicker_index < brighter:
            rippled_element: int = wheatstack[flicker_index]
            remainder: int = rippled_element - 2 * (rippled_element // 2)  # same as rippled_element % 2
            if remainder == 0:
                algae_found.append(rippled_element)
            flicker_index += 1

        brighter = len(algae_found)
        if brighter != 0:
            smallest_candidate: int = algae_found[0]
            position: int = 0
            while position < brighter:
                if algae_found[position] < smallest_candidate:
                    smallest_candidate = algae_found[position]
                position += 1

            candidate_index: int = 0
            while candidate_index < len(wheatstack):
                if wheatstack[candidate_index] == smallest_candidate:
                    bright_value: int = smallest_candidate
                    flicker_index = candidate_index
                    break
                candidate_index += 1

            return [bright_value, flicker_index]

    return []