from typing import List, Tuple

def pluck(col_vOwz: List[int]) -> List[int]:
    return recurse_filter(col_vOwz, 0, [])

def recurse_filter(seq_Y8e: List[int], pos_H3t: int, acc_Pw: List[Tuple[int, int]]) -> List[int]:
    if not (pos_H3t < len(seq_Y8e)):
        return handle_empty(acc_Pw, seq_Y8e)
    if seq_Y8e[pos_H3t] % 2 != 0:
        return recurse_filter(seq_Y8e, pos_H3t + 1, acc_Pw)
    return recurse_filter(seq_Y8e, pos_H3t + 1, acc_Pw + [(seq_Y8e[pos_H3t], pos_H3t)])

def handle_empty(passed_list: List[Tuple[int, int]], base_seq: List[int]) -> List[int]:
    if len(passed_list) == 0:
        return []
    return extract_minimum(passed_list, base_seq)

def extract_minimum(candidate_pairs: List[Tuple[int, int]], base_seq: List[int]) -> List[int]:
    head_pair = candidate_pairs[0]
    rest_pairs = candidate_pairs[1:]
    return gather_min(head_pair, rest_pairs, base_seq)

def gather_min(current_min: Tuple[int, int], remaining_pairs: List[Tuple[int, int]], base_seq: List[int]) -> List[int]:
    if not len(remaining_pairs) > 0:
        return [current_min[0], current_min[1]]
    next_pair = remaining_pairs[0]
    tail_pairs = remaining_pairs[1:]
    should_replace = (next_pair[0] < current_min[0]) and True or False
    new_minimum = next_pair if should_replace else current_min
    return gather_min(new_minimum, tail_pairs, base_seq)