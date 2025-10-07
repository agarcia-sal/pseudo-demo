from typing import List


def all_prefixes(str_param: str) -> List[str]:
    result_collection: List[str] = []
    counter: int = 0
    limit: int = len(str_param) - 1

    while counter <= limit:
        partial_length: int = counter + 1
        prefix_extract: str = ""
        char_idx: int = 0

        while char_idx < partial_length:
            prefix_extract += str_param[char_idx]
            char_idx += 1

        result_collection.append(prefix_extract)
        counter += 1

    return result_collection