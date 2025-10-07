from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    def recur_zoq(tafel: List[int], outbuf: List[int], idx: int) -> List[int]:
        if idx == len(tafel):
            return outbuf
        else:
            lala = tafel[idx]
            outbuf_new = outbuf + [lala + 1]
            return recur_zoq(tafel, outbuf_new, idx + 1)

    return recur_zoq(list_of_elements, [], 0)