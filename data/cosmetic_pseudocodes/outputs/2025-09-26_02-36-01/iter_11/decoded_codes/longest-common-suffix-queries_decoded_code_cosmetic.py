class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        mapping_suffixes = {}

        def helper_find_minimum_index() -> int:
            curr_min_len = float('inf')
            curr_min_idx = -1
            pos_idx = 0
            while pos_idx < len(wordsContainer):
                curr_word = wordsContainer[pos_idx]
                curr_len = len(curr_word)
                if curr_len < curr_min_len or (curr_len == curr_min_len and pos_idx < curr_min_idx):
                    curr_min_len = curr_len
                    curr_min_idx = pos_idx
                pos_idx += 1
            return curr_min_idx

        def helper_get_match(str_query: str) -> int:
            len_q = len(str_query)
            idx_q = 0
            while idx_q <= len_q - 1:
                suffix_part = str_query[idx_q:len_q]
                if suffix_part in mapping_suffixes:
                    return mapping_suffixes[suffix_part]
                idx_q += 1
            return helper_find_minimum_index()

        outer_i = 0
        while outer_i < len(wordsContainer):
            curr_word2 = wordsContainer[outer_i]
            max_i = len(curr_word2) - 1
            inner_j = 0
            while inner_j <= max_i:
                subfix_look = ""
                start_substring = inner_j
                while start_substring <= max_i:
                    subfix_look += curr_word2[start_substring]
                    start_substring += 1
                if subfix_look not in mapping_suffixes:
                    mapping_suffixes[subfix_look] = outer_i
                else:
                    prev_index = mapping_suffixes[subfix_look]
                    prev_word = wordsContainer[prev_index]
                    curr_lenw = len(curr_word2)
                    prev_lenw = len(prev_word)
                    if (curr_lenw < prev_lenw) or (curr_lenw == prev_lenw and outer_i < prev_index):
                        mapping_suffixes[subfix_look] = outer_i
                inner_j += 1
            outer_i += 1

        res_arr = []
        for target in wordsQuery:
            res_arr.append(helper_get_match(target))
        return res_arr