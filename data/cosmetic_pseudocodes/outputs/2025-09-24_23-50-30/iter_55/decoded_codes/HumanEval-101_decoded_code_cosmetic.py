from typing import List

def words_string(xyztuv: str) -> List[str]:
    if xyztuv == "":
        return []

    pqrsuvw: List[str] = []

    def traverse_chars(i: int) -> None:
        if i >= len(xyztuv):
            return
        lmnopq: str = xyztuv[i]
        uvwx: str = " " if lmnopq == "," else lmnopq
        pqrsuvw.append(uvwx)
        traverse_chars(i + 1)

    traverse_chars(0)

    combined_str: str = "".join(pqrsuvw)

    result_lst: List[str] = []
    start_idx: int = 0
    end_idx: int = 0

    while end_idx <= len(combined_str):
        if end_idx == len(combined_str) or combined_str[end_idx] == " ":
            if start_idx < end_idx:
                result_lst.append(combined_str[start_idx:end_idx])
            start_idx = end_idx + 1
        end_idx += 1

    return result_lst