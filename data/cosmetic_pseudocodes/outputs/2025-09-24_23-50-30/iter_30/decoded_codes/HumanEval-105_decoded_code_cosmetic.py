from typing import Sequence, List

def by_length(data_sequence: Sequence[int]) -> List[str]:
    mapping_table: dict[int, str] = {
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
    # Sort descending
    descending_seq = sorted(data_sequence, reverse=True)
    output_buffer: List[str] = []
    for index in range(len(descending_seq)):
        val = descending_seq[index]
        if val in mapping_table:
            output_buffer.append(mapping_table[val])
        else:
            continue
    return output_buffer