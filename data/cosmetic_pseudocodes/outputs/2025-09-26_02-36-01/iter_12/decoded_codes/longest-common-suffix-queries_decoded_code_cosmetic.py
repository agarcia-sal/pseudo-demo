class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        map_suffixes = {}

        def compute_substring(str_val: str, startPos: int) -> str:
            return str_val[startPos:]

        def is_shorter_or_equal_length_and_smaller_index(a_index: int, b_index: int) -> bool:
            len_a = len(wordsContainer[a_index])
            len_b = len(wordsContainer[b_index])
            if len_a < len_b:
                return True
            if len_a == len_b:
                return a_index < b_index
            return False

        for iterator_outer, current_word in enumerate(wordsContainer):
            for iterator_inner in range(len(current_word)):
                current_suffix = compute_substring(current_word, iterator_inner)
                if current_suffix not in map_suffixes:
                    map_suffixes[current_suffix] = iterator_outer
                else:
                    stored_index = map_suffixes[current_suffix]
                    if is_shorter_or_equal_length_and_smaller_index(iterator_outer, stored_index):
                        map_suffixes[current_suffix] = iterator_outer

        def get_best_match(query: str) -> int:
            length_query = len(query)
            position = 0
            while position < length_query:
                suffix = compute_substring(query, position)
                if suffix in map_suffixes:
                    return map_suffixes[suffix]
                position += 1

            min_index = 0
            min_length = len(wordsContainer[0])
            for pointer in range(1, len(wordsContainer)):
                candidate_length = len(wordsContainer[pointer])
                if candidate_length < min_length:
                    min_length = candidate_length
                    min_index = pointer
                elif candidate_length == min_length and pointer < min_index:
                    min_index = pointer
            return min_index

        def append_element_to_list(list_ref: list[int], val: int):
            list_ref.append(val)

        collected_results = []
        for idx_query in range(len(wordsQuery)):
            append_element_to_list(collected_results, get_best_match(wordsQuery[idx_query]))

        return collected_results