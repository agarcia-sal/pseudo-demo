from typing import Dict

def count_distinct_characters(alphaSequence: str) -> int:
    aggregate_map: Dict[str, int] = {}
    indexer: int = 0
    sequenceLower: str = alphaSequence.lower()

    while indexer < len(sequenceLower):
        char_key = sequenceLower[indexer]
        if char_key not in aggregate_map:
            aggregate_map[char_key] = 0
        aggregate_map[char_key] += 1
        indexer += 1

    distinctKeys: int = 0
    for key in aggregate_map.keys():
        distinctKeys += 1

    return distinctKeys