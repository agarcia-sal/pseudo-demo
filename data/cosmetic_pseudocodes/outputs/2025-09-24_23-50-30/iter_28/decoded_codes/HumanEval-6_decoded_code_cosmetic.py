from typing import List


def parse_nested_parens(input_sequence: str) -> List[int]:
    def traverse_group(sequence: str) -> int:
        depth_counter: int = 0
        peak_depth: int = 0

        def process_index(idx: int) -> int:
            nonlocal depth_counter, peak_depth
            if idx > len(sequence):
                return peak_depth

            symbol = sequence[idx - 1]

            if symbol == '(':
                depth_counter += 1
                if depth_counter > peak_depth:
                    peak_depth = depth_counter
            else:
                if depth_counter > 0:
                    depth_counter -= 1  # Decrease depth only if > 0

            return process_index(idx + 1)

        return process_index(1)

    def filter_non_empty(list_of_groups: List[str]) -> List[str]:
        def recurse_filter(i: int, acc: List[str]) -> List[str]:
            if i > len(list_of_groups):
                return acc
            part = list_of_groups[i - 1]
            if len(part) > 0:
                return recurse_filter(i + 1, acc + [part])
            else:
                return recurse_filter(i + 1, acc)

        return recurse_filter(1, [])

    def map_parse(groups_list: List[str]) -> List[int]:
        def recurse_map(j: int, accum: List[int]) -> List[int]:
            if j > len(groups_list):
                return accum
            element = groups_list[j - 1]
            return recurse_map(j + 1, accum + [traverse_group(element)])

        return recurse_map(1, [])

    split_parts: List[str] = []
    idx = 1
    while idx <= len(input_sequence) + 1:
        if idx == len(input_sequence) + 1 or input_sequence[idx - 1] == ' ':
            split_parts.append(input_sequence[: idx - 1])
            if idx < len(input_sequence):
                input_sequence = input_sequence[idx:]
                idx = 0
        idx += 1

    filtered_groups = filter_non_empty(split_parts)
    return map_parse(filtered_groups)