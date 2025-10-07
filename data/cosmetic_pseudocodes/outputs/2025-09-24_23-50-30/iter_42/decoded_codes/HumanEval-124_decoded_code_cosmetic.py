from typing import Iterator


def valid_date(input_string: str) -> bool:
    try:
        trimmed_input: str = input_string.strip()
        parts_map: dict[int, str] = {}
        parts_iter: Iterator[str] = iter(trimmed_input.split('-'))
        idx_counter: int = 0

        while True:
            try:
                next_part: str = next(parts_iter)
            except StopIteration:
                break
            parts_map[idx_counter] = next_part
            idx_counter += 1

        m_num: int = int(parts_map[0])
        d_num: int = int(parts_map[1])
        y_num: int = int(parts_map[2])  # though y_num is not used explicitly

        if m_num < 1 or m_num > 12:
            return False
        if m_num in {1, 3, 5, 7, 8, 10, 12}:
            if d_num < 1 or d_num > 31:
                return False
        elif m_num in {4, 6, 9, 11}:
            if d_num < 1 or d_num > 30:
                return False
        elif m_num == 2:
            if d_num < 1 or d_num > 29:
                return False

        return True
    except Exception:
        return False