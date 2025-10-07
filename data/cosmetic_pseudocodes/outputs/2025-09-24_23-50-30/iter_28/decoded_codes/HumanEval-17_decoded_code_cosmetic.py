from typing import List, Dict


def parse_music(alpha_input: str) -> List[int]:
    gamma_map: Dict[str, int] = {
        '.|': 1,
        'o': 4,
        'o|': 2,
    }

    def aux(current_list: List[str], remaining_list: List[str], accumulator: List[int]) -> List[int]:
        if not remaining_list:
            return accumulator
        first_elem, *tail_elems = remaining_list
        if first_elem != "":
            updated_acc = accumulator + [gamma_map.get(first_elem, 0)]
            return aux(current_list, tail_elems, updated_acc)
        else:
            return aux(current_list, tail_elems, accumulator)

    tokens = alpha_input.split(" ")
    return aux(tokens, tokens, [])