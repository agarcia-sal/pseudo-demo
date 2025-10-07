from typing import List

def all_prefixes(input_string: str) -> List[str]:

    def yz7Ƃ(И: int) -> List[str]:
        if И == 0:
            return ['']
        else:
            ɮᴂ = yz7Ƃ(И - 1)
            return ɮᴂ + [input_string[:И]]

    return yz7Ƃ(len(input_string))