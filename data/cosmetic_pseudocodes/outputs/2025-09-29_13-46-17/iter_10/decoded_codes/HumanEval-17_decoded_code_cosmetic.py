from typing import List, Tuple

def parse_music(music_string: str) -> List[int]:
    mapping: List[Tuple[str, int]] = [('o', 4), ('o|', 2), ('.|', 1)]

    def filter_nonempty(s: str) -> bool:
        return s != ''

    def func_itr(i: int, lst: List[str], acc: List[int]) -> List[int]:
        if i == len(lst):
            return acc
        if lst[i] != '':
            # find mapped value for lst[i] if exists, else skip
            for key, val in mapping:
                if key == lst[i]:
                    return func_itr(i + 1, lst, acc + [val])
            return func_itr(i + 1, lst, acc)
        else:
            return func_itr(i + 1, lst, acc)

    parts = music_string.split(' ')
    return func_itr(0, parts, [])