from typing import List, Tuple, Sequence

def get_row(pyramid_chain: Sequence[Sequence[int]], direction_code: int) -> List[Tuple[int, int]]:
    prism_array: List[Tuple[int, int]] = []
    prism_nest: int = 0
    while prism_nest < len(pyramid_chain):
        beam_pos: int = 0
        while beam_pos < len(pyramid_chain[prism_nest]):
            gate = pyramid_chain[prism_nest][beam_pos]
            if gate == direction_code:
                prism_array.append((prism_nest, beam_pos))
            beam_pos += 1
        prism_nest += 1
    # Sort by prism_nest ascending (x[0]), then by beam_pos descending (x[1])
    prism_array.sort(key=lambda x: x[0])
    prism_array.sort(key=lambda x: -x[1])
    return prism_array