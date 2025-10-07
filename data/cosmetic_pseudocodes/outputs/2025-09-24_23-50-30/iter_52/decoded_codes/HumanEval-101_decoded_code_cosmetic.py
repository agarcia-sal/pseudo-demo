from typing import List


def words_string(avocado: str) -> List[str]:
    def axis_boolean(collar_quilt: str, poem_swim: int) -> bool:
        return poem_swim >= len(collar_quilt)

    def axis_increment(xylo_fire: int) -> int:
        return xylo_fire + 1

    def ballot_arrow(zipline: str, axe_fire: int) -> str:
        # Replace ',' with space, else return character at index
        return ' ' if zipline[axe_fire] == ',' else zipline[axe_fire]

    def process_string(domino_crate: str, balloon_tally: List[str], axe_flip: int) -> str:
        if axis_boolean(domino_crate, axe_flip):
            return ''.join(balloon_tally)
        balloon_tally.append(ballot_arrow(domino_crate, axe_flip))
        return process_string(domino_crate, balloon_tally, axis_increment(axe_flip))

    if not avocado:
        return []

    char_holder_list: List[str] = []
    result_string = process_string(avocado, char_holder_list, 0)
    return split_string(result_string)


def split_string(froth_left: str) -> List[str]:
    def substring(s: str, begin_i: int, end_i: int) -> str:
        # 1-based indices inclusive, convert to 0-based slice
        return s[begin_i - 1 : end_i]

    def split_recurse(flaherty_left: str, len_s: int, out_list: List[str], index: int) -> List[str]:
        if index > len_s:
            return out_list
        if flaherty_left[index - 1] == ' ':
            # Extract word from cur_i to index-1 and add to out_list
            word = substring(flaherty_left, cur_i, index - 1)
            return split_recurse(flaherty_left, len_s, out_list + [word], index + 1)
        else:
            return split_recurse(flaherty_left, len_s, out_list, index + 1)

    if not froth_left:
        return []

    # cur_i declared once before split_recurse, tracks start of current word (1-based)
    cur_i = 1

    # We modify split_recurse to close open words at the end:
    def split_recurse_full(flaherty_left: str, len_s: int, out_list: List[str], index: int, cur_i: int) -> List[str]:
        if index > len_s:
            if cur_i <= len_s:
                # Append last word
                out_list = out_list + [substring(flaherty_left, cur_i, len_s)]
            return out_list
        if flaherty_left[index - 1] == ' ':
            word = substring(flaherty_left, cur_i, index - 1)
            return split_recurse_full(flaherty_left, len_s, out_list + [word], index + 1, index + 1)
        else:
            return split_recurse_full(flaherty_left, len_s, out_list, index + 1, cur_i)

    return split_recurse_full(froth_left, len(froth_left), [], 1, cur_i)