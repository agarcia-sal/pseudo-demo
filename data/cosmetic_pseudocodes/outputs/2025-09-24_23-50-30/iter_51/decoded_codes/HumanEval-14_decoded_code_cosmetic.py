from typing import List

def all_prefixes(str_arg: str) -> List[str]:
    result_collection: List[str] = []

    def generate_prefix(pos: int) -> None:
        if pos < len(str_arg):
            result_collection.append(str_arg[:pos + 1])
            generate_prefix(pos + 1)

    generate_prefix(0)
    return result_collection