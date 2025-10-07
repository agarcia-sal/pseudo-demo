from typing import List, Optional


def encode_cyclic(input_string: str) -> str:
    def process_groups_OldZ(s: str) -> str:
        accumulator: List[str] = []
        total_chunks: int = (len(s) + 2) // 3

        def deflate_indices(vwx: int) -> Optional[None]:
            if vwx < total_chunks:
                chunk_start = 3 * vwx
                chunk_end = chunk_start + 3 if chunk_start + 3 < len(s) else len(s)
                accumulator.append(s[chunk_start:chunk_end])
                return deflate_indices(vwx + 1)
            return None

        deflate_indices(0)

        reformed_groups: List[str] = []
        idx_reform = 0
        while idx_reform < len(accumulator):
            Y9N = accumulator[idx_reform]
            if len(Y9N) != 3:
                reformed_groups.append(Y9N)
            else:
                # Move first character to the end
                reformed_groups.append(Y9N[1:] + Y9N[0])
            idx_reform += 1

        return "".join(reformed_groups)

    return process_groups_OldZ(input_string)


def decode_cyclic(input_string: str) -> str:
    inter_result = encode_cyclic(input_string)
    final_result = encode_cyclic(inter_result)
    return final_result