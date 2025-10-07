from typing import Dict

def same_chars(sequence_alpha: str, sequence_beta: str) -> bool:
    def build_character_map(text_input: str) -> Dict[str, bool]:
        def recursive_map(index: int, accumulator: Dict[str, bool]) -> Dict[str, bool]:
            if index < 0:
                return accumulator
            current_character = text_input[index]
            accumulator[current_character] = True
            return recursive_map(index - 1, accumulator)
        return recursive_map(len(text_input) - 1, {})

    def maps_equal(map_one: Dict[str, bool], map_two: Dict[str, bool]) -> bool:
        def keys_equal(list_one: list[str], list_two: list[str]) -> bool:
            if len(list_one) != len(list_two):
                return False
            def check_all(i: int) -> bool:
                if i == len(list_one):
                    return True
                if list_one[i] in map_two:
                    return check_all(i + 1)
                return False
            return check_all(0)
        return keys_equal(list(map_one.keys()), list(map_two.keys()))

    return maps_equal(build_character_map(sequence_alpha), build_character_map(sequence_beta))