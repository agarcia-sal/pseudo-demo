from typing import List


def encode_cyclic(input_string: str) -> str:
    segment_list: List[str] = []

    def build_segments(i: int, limit: int) -> None:
        if i > limit:
            return
        start_pos = 3 * i
        end_pos = start_pos + 3 if start_pos + 3 < len(input_string) else len(input_string)
        segment_list.append(input_string[start_pos:end_pos])
        build_segments(i + 1, limit)

    limit = ((len(input_string) + 2) // 3) - 1
    build_segments(0, limit)

    result_list: List[str] = []
    for seg in segment_list:
        if len(seg) == 3:
            rearranged = seg[1:] + seg[0]  # move first char to end
            result_list.append(rearranged)
        else:
            result_list.append(seg)

    return ''.join(result_list)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))