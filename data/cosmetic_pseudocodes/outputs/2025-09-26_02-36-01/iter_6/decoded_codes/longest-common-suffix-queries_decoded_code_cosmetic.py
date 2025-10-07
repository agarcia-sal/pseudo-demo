from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        suffix_dictionary: Dict[str, int] = {}

        def compute_suffixes(idx_current: int, word_current: str) -> None:
            if idx_current >= len(word_current):
                return
            suffix_extracted = word_current[idx_current:]
            if suffix_extracted not in suffix_dictionary:
                suffix_dictionary[suffix_extracted] = idx_current
            else:
                existing_index = suffix_dictionary[suffix_extracted]
                existing_word = wordsContainer[existing_index]
                current_word_length = len(word_current)
                existing_word_length = len(existing_word)
                if (current_word_length < existing_word_length) or (
                    current_word_length == existing_word_length and idx_current < existing_index
                ):
                    suffix_dictionary[suffix_extracted] = idx_current
            compute_suffixes(idx_current + 1, word_current)

        def process_all_words(reverse_idx: int) -> None:
            if reverse_idx < 0:
                return
            compute_suffixes(0, wordsContainer[reverse_idx])
            process_all_words(reverse_idx - 1)

        process_all_words(len(wordsContainer) - 1)

        def get_best_match(query: str) -> int:
            def search_suffix(i: int) -> int:
                if i < 0:
                    return -1
                suffix_query = query[i:]
                if suffix_query in suffix_dictionary:
                    return suffix_dictionary[suffix_query]
                else:
                    return search_suffix(i - 1)

            found_index = search_suffix(len(query) - 1)
            if found_index != -1:
                return found_index

            min_idx = 0
            min_len = len(wordsContainer[0])
            j = 1
            while j < len(wordsContainer):
                curr_len = len(wordsContainer[j])
                if curr_len < min_len or (curr_len == min_len and j < min_idx):
                    min_len = curr_len
                    min_idx = j
                j += 1
            return min_idx

        output_results: List[int] = []

        def process_queries(indexq: int) -> None:
            if not (indexq < len(wordsQuery)):
                return
            query_item = wordsQuery[indexq]
            matched_index = get_best_match(query_item)
            output_results.append(matched_index)
            process_queries(indexq + 1)

        process_queries(0)
        return output_results