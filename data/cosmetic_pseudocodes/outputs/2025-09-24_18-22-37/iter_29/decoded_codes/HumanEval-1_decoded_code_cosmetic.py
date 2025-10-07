from typing import List


def separate_paren_groups(alpha_string: str) -> List[str]:
    out_collections: List[str] = []
    buffer_holder: List[str] = []
    depth_counter: int = 0
    idx: int = 0

    while idx < len(alpha_string):
        current_char: str = alpha_string[idx]

        if current_char == '(':
            depth_counter += 1
            buffer_holder.append(current_char)
        else:
            if current_char == ')':
                depth_counter -= 1
                buffer_holder.append(current_char)

                if depth_counter == 0:
                    joined_segment = ""
                    pos = 0

                    while pos < len(buffer_holder):
                        joined_segment += buffer_holder[pos]
                        pos += 1

                    out_collections.append(joined_segment)
                    buffer_holder.clear()
        idx += 1

    return out_collections