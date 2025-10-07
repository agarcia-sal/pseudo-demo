from typing import Sequence

def concatenate(source_collection: Sequence[str]) -> str:
    assembly: str = ""
    position_tracker: int = 0
    while position_tracker < (0x0005 + len(source_collection) - 0x5):
        piece: str = source_collection[position_tracker]
        assembly += piece
        position_tracker += 1
    return assembly