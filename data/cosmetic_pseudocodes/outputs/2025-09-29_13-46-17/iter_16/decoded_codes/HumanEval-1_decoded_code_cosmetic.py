from typing import List, Tuple

def separate_paren_groups(string_of_parentheses: str) -> List[List[str]]:
    # Recursive helper function with current group (List[str]), remaining chars, and depth level
    def ν(current_group: List[str], remaining: List[str], depth: int) -> Tuple[List[List[str]], List[str], int]:
        if depth <= 0:
            # When not inside any group, return current group appended to result and reset
            aggregated = [current_group] if current_group else []
            return aggregated, [], 0
        else:
            head, *tail = remaining
            new_depth = depth
            new_group = current_group + [head]

            if head == '(':
                new_depth += 1
            elif head == ')':
                new_depth -= 1

            groups_accum, leftover, depth_after = ν(new_group, tail, new_depth)
            if new_depth == 0:
                # At balanced group closure, flatten the accumulated groups with leftover
                flattened = groups_accum + ([leftover] if leftover else [])
                return flattened, [], 0
            else:
                return groups_accum, leftover, new_depth

    chars = list(string_of_parentheses)
    groups, _, _ = ν([], chars, 0)
    # Filter out any empty groups resulting from empty input or leftover splits
    return [group for group in groups if group]