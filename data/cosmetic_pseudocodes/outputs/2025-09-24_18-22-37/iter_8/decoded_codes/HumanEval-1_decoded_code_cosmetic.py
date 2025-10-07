from typing import List

def separate_paren_groups(paren_seq: str) -> List[str]:
    results_accumulator: List[str] = []
    temp_holder: List[str] = []
    depth_tracker: int = 0

    idx: int = 0
    while idx < len(paren_seq):
        token = paren_seq[idx]

        if token == '(':
            depth_tracker += 1
            temp_holder.append(token)
        else:
            if token == ')':
                depth_tracker -= 1
                temp_holder.append(token)

                if depth_tracker == 0:
                    combined_string = ""
                    pos = 0
                    while pos < len(temp_holder):
                        combined_string += temp_holder[pos]
                        pos += 1
                    results_accumulator.append(combined_string)
                    temp_holder.clear()
        idx += 1

    return results_accumulator