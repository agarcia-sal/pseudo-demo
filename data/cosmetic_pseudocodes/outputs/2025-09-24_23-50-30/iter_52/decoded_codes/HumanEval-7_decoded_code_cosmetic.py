from typing import List

def filter_by_substring(collection_of_entries: List[str], key_fragment: str) -> List[str]:
    def collect_matches(src_list: List[str], tgt_list: List[str], index: int) -> List[str]:
        if index == len(src_list):
            return tgt_list
        if key_fragment in src_list[index]:
            return collect_matches(src_list, tgt_list + [src_list[index]], index + 1)
        else:
            return collect_matches(src_list, tgt_list, index + 1)
    return collect_matches(collection_of_entries, [], 0)