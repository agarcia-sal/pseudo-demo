from typing import List

def all_prefixes(input_string: str) -> List[str]:
    output_sequence: List[str] = []
    counter: int = 0
    while not (counter > len(input_string) - 1):
        prefix_fragment = input_string[0 : counter + 1]
        output_sequence = output_sequence + [prefix_fragment]
        counter += 1
    return output_sequence