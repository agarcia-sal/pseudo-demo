from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        suffix_map: Dict[str, int] = {}

        # Precompute the suffix map with the smallest index word having the suffix preferring shorter words and smaller indices
        for index, word in enumerate(wordsContainer):
            length_word = len(word)
            for i in range(length_word):
                suffix = word[i:]
                if suffix not in suffix_map:
                    suffix_map[suffix] = index
                else:
                    current_index = suffix_map[suffix]
                    current_word = wordsContainer[current_index]
                    # Update if current word is longer or same length but index is bigger
                    if (length_word < len(current_word)) or (length_word == len(current_word) and index < current_index):
                        suffix_map[suffix] = index

        def get_best_match(query: str) -> int:
            length_query = len(query)
            for i in range(length_query):
                suffix = query[i:]
                if suffix in suffix_map:
                    return suffix_map[suffix]

            # If no suffix match, find the index of the smallest length word, earliest occurrence in wordsContainer
            min_index = 0
            min_length = len(wordsContainer[0])
            for idx, word in enumerate(wordsContainer):
                if len(word) < min_length or (len(word) == min_length and idx < min_index):
                    min_length = len(word)
                    min_index = idx
            return min_index

        result_list: List[int] = []
        for query in wordsQuery:
            result_list.append(get_best_match(query))

        return result_list