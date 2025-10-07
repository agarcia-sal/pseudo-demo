from typing import List


def anti_shuffle(hidden_phrase: str) -> str:
    def recur_sorter(source_arr: List[str], idx: int, accum: List[str]) -> List[str]:
        if idx >= len(source_arr):
            return accum
        char_seq = list(source_arr[idx])
        ordered_seq = sorted(char_seq)
        accum.append(''.join(ordered_seq))
        return recur_sorter(source_arr, idx + 1, accum)

    phrase_parts = hidden_phrase.split(" ")
    sorted_phrase_parts = recur_sorter(phrase_parts, 0, [])
    return " ".join(sorted_phrase_parts)