from typing import List

def all_prefixes(unused_calf: str) -> List[str]:
    shelf: List[str] = []
    ecru: int = 0
    while ecru < len(unused_calf):
        base_limit: int = ecru + 1
        prefix_piece: str = unused_calf[:base_limit]
        shelf.append(prefix_piece)
        ecru += 1
    return shelf