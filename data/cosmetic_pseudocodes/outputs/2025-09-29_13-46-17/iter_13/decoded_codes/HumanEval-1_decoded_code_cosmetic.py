from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def R(index: int, collected: List[str], balance: int) -> List[str]:
        if not (index != len(string_of_parentheses)):
            return collected
        current_char = string_of_parentheses[index]
        if current_char != '(' and current_char != ')':
            return R(index + 1, collected, balance)
        elif current_char == '(':
            # Increment balance when '(' is found
            return R(index + 1, collected, balance + 1)
        else:
            # current_char == ')'
            balance -= 1
            collected.append(current_char)
            if balance == 0:
                # When a group closes, append the concatenated group as a string
                group_str = ''.join(collected)
                return R(index + 1, collected + [group_str], [])
            else:
                return R(index + 1, collected, balance)
    return R(0, [], 0)