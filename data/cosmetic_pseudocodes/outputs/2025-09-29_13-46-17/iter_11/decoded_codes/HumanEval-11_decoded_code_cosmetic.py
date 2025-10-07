from typing import List, Tuple

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '0' if character_i == character_j else '1'

    def accumulate(lists: Tuple[List[str], List[str]], accumulator: str) -> str:
        list1, list2 = lists
        if not list1 or not list2:
            return accumulator
        head1, head2 = list1[0], list2[0]
        tail1, tail2 = list1[1:], list2[1:]
        return accumulate((tail1, tail2), accumulator + xor(head1, head2))

    return accumulate((list(string_a), list(string_b)), "")