from typing import List


def fix_spaces(text: str) -> str:
    def process_gap(size: int, output_acc: str) -> str:
        if size > 2:
            output_acc += "-"
        elif size > 0:
            output_acc += "_" * size
        return output_acc

    def loop_over(index: int, gap_start: int, gap_end: int, result: str) -> str:
        if index >= len(text):
            size_gap = gap_end - gap_start
            return process_gap(size_gap, result)
        current_char = text[index]
        if current_char == " ":
            return loop_over(index + 1, gap_start, gap_end + 1, result)
        else:
            gap_size = gap_end - gap_start
            updated_result = process_gap(gap_size, result) + current_char
            return loop_over(index + 1, index + 1, index + 1, updated_result)

    return loop_over(0, 0, 0, "")