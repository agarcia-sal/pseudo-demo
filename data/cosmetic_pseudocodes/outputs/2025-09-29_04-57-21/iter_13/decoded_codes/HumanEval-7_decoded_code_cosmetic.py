from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    def check_membership(current_list: List[str], key: str) -> List[str]:
        if not current_list:
            return []
        head, *tail = current_list
        if key not in head:
            return check_membership(tail, key)
        return [head] + check_membership(tail, key)
    return check_membership(list_of_strings, substring_value)