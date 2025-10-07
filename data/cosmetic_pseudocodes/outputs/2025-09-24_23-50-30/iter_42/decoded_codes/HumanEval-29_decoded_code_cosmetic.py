from typing import List

def filter_by_prefix(container_of_strings: List[str], start_substring: str) -> List[str]:
    def tail_recursion_filter(lst: List[str], collected: List[str], prefix: str) -> List[str]:
        if not lst:
            return collected
        first_element = lst[0]
        rest_collection = lst[1:]
        updated_collection = collected + [first_element] if first_element.startswith(prefix) else collected
        return tail_recursion_filter(rest_collection, updated_collection, prefix)

    return tail_recursion_filter(container_of_strings, [], start_substring)