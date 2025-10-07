from typing import List, Tuple

def string_xor(string_p: str, string_q: str) -> str:
    def inner_xor(char_m: str, char_n: str) -> str:
        # Returns '0' if chars are equal, else '1'
        return '0' if char_m == char_n else '1'

    def fold_xor(pair_list: List[Tuple[str, str]], acc_str: str) -> str:
        if not pair_list:
            return acc_str
        head_pair, *tail_pairs = pair_list
        new_acc = acc_str + inner_xor(head_pair[0], head_pair[1])
        return fold_xor(tail_pairs, new_acc)

    min_length = min(len(string_p), len(string_q))
    zipped_pairs: List[Tuple[str, str]] = [(string_p[i], string_q[i]) for i in range(min_length)]
    return fold_xor(zipped_pairs, "")