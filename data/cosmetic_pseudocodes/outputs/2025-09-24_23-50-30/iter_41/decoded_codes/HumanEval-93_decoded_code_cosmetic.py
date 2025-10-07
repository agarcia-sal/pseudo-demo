from typing import Dict, List

def encode(input: str) -> str:
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    trans_map: Dict[str, str] = {}

    def build_map(idx: int, arr: List[str]) -> None:
        if idx >= len(arr):
            return
        ch = arr[idx]
        trans_map[ch] = chr(ord(ch) + 2)
        build_map(idx + 1, arr)

    build_map(0, list("aeiouAEIOU"))

    def swap_case_rec(i: int, accum: str) -> str:
        if i == len(input):
            return accum
        c = input[i]
        accum2 = accum + (c.lower() if c in vowels_set else c.upper())
        return swap_case_rec(i + 1, accum2)

    swapped_message = swap_case_rec(0, "")

    def transform_chars(lst: List[str], idx: int, acc: str) -> str:
        if idx == len(lst):
            return acc
        current = lst[idx]
        val = trans_map[current] if current in trans_map else current
        return transform_chars(lst, idx + 1, acc + val)

    char_list = list(swapped_message)
    return transform_chars(char_list, 0, "")