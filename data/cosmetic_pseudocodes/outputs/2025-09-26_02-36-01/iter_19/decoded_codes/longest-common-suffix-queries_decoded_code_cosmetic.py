from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        map_suffixes: Dict[str, int] = {}

        for idx_outer, element_word in enumerate(wordsContainer):
            for pos_inner in range(len(element_word)):
                substr_suffix = element_word[pos_inner:]
                if substr_suffix not in map_suffixes:
                    map_suffixes[substr_suffix] = idx_outer
                else:
                    stored_idx = map_suffixes[substr_suffix]
                    stored_word = wordsContainer[stored_idx]
                    if (len(element_word) < len(stored_word)) or (
                        len(element_word) == len(stored_word) and idx_outer < stored_idx
                    ):
                        map_suffixes[substr_suffix] = idx_outer

        def get_best_match(query: str) -> int:
            len_query = len(query)
            for pos_i in range(len_query):
                suff_substr = query[pos_i:]
                if suff_substr in map_suffixes:
                    return map_suffixes[suff_substr]

            min_len = len(wordsContainer[0])
            min_index = 0
            for j, curr_word in enumerate(wordsContainer[1:], start=1):
                if (len(curr_word) < min_len) or (
                    len(curr_word) == min_len and j < min_index
                ):
                    min_len = len(curr_word)
                    min_index = j
            return min_index

        list_results: List[int] = []
        for query_element in wordsQuery:
            list_results.append(get_best_match(query_element))

        return list_results