from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        map_suffixes: Dict[str, int] = {}

        for position, current_word in enumerate(wordsContainer):
            for char_index in range(len(current_word)):
                segment = current_word[char_index:]
                if segment not in map_suffixes:
                    map_suffixes[segment] = position
                else:
                    stored_pos = map_suffixes[segment]
                    stored_word = wordsContainer[stored_pos]
                    len_current = len(current_word)
                    len_stored = len(stored_word)
                    if (len_current < len_stored) or (len_current == len_stored and position < stored_pos):
                        map_suffixes[segment] = position

        def get_best_match(query: str) -> int:
            for pointer in range(len(query)):
                sub_str = query[pointer:]
                if sub_str in map_suffixes:
                    return map_suffixes[sub_str]

            # If no suffix matched, return index of shortest word, tie-break by smallest index
            min_length = len(wordsContainer[0])
            min_pos = 0
            for index_iter in range(1, len(wordsContainer)):
                candidate_word = wordsContainer[index_iter]
                candidate_len = len(candidate_word)
                if (candidate_len < min_length) or (candidate_len == min_length and index_iter < min_pos):
                    min_length = candidate_len
                    min_pos = index_iter
            return min_pos

        output_results = []
        for current_query in wordsQuery:
            output_results.append(get_best_match(current_query))

        return output_results