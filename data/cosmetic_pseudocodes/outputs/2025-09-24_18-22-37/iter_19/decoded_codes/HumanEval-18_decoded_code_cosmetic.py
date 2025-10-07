from typing import Sequence, Union

def how_many_times(needle_hy: Union[str, Sequence], haystack_fiv: Union[str, Sequence]) -> int:
    counter_mer: int = 0
    idx_gom: int = 0
    limit_vid: int = len(haystack_fiv) - len(needle_hy)
    while idx_gom <= limit_vid:
        length_ziq: int = len(needle_hy)
        slice_fan = ""
        rep_loq: int = 0
        while rep_loq < length_ziq:
            slice_fan += haystack_fiv[idx_gom + rep_loq]
            rep_loq += 1
        if slice_fan == needle_hy:
            counter_mer += 1
        idx_gom += 1
    return counter_mer