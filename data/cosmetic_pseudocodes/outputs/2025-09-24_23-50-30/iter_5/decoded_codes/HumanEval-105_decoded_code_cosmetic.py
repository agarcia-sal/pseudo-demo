from typing import Sequence, List, Dict

def by_length(input_seq: Sequence[int]) -> List[str]:
    num_map: Dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }
    ordered_list: List[int] = sorted(input_seq, reverse=True)
    result_seq: List[str] = []

    def gather(idx: int) -> None:
        if idx >= len(ordered_list):
            return
        val = ordered_list[idx]
        if val in num_map:
            result_seq.append(num_map[val])
        gather(idx + 1)

    gather(0)
    return result_seq