import re
from typing import List

def is_bored(string_argument: str) -> int:
    segments_collection: List[str] = re.split(r'[.?!]\s*', string_argument)
    total_boredom_count: int = 0
    idx_counter: int = 0
    while idx_counter < len(segments_collection):
        current_segment: str = segments_collection[idx_counter]
        temp_match_flag: int = 1 if current_segment.startswith('I ') else 0
        total_boredom_count += temp_match_flag
        idx_counter += 1
    return total_boredom_count