from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        mapping_suffixes: Dict[str, int] = {}

        def recordSuffixIndex(str_current: str, idx_cur: int):
            def loop_suffixes(pos: int):
                if pos > len(str_current) - 1:
                    return
                current_suffix = str_current[pos:]
                if current_suffix in mapping_suffixes:
                    prev_index = mapping_suffixes[current_suffix]
                    prev_word = wordsContainer[prev_index]
                    # Update index if current word is shorter or same length but smaller index
                    if (len(str_current) < len(prev_word)) or (
                            len(str_current) == len(prev_word) and idx_cur < prev_index):
                        mapping_suffixes[current_suffix] = idx_cur
                else:
                    mapping_suffixes[current_suffix] = idx_cur
                loop_suffixes(pos + 1)

            loop_suffixes(0)

        def findOptimalIndex(query_string: str) -> int:
            def searchSuffix(posq: int) -> int:
                if posq > len(query_string) - 1:
                    return -1
                sub_suf = query_string[posq:]
                if sub_suf in mapping_suffixes:
                    return mapping_suffixes[sub_suf]
                else:
                    return searchSuffix(posq + 1)

            found_index = searchSuffix(0)
            if found_index != -1:
                return found_index

            def minIndexByLength(idx_start: int, cur_min_idx: int) -> int:
                if idx_start > len(wordsContainer) - 1:
                    return cur_min_idx
                candidate_word = wordsContainer[idx_start]
                best_word = wordsContainer[cur_min_idx]
                if (len(candidate_word) < len(best_word)) or (
                        len(candidate_word) == len(best_word) and idx_start < cur_min_idx):
                    return minIndexByLength(idx_start + 1, idx_start)
                else:
                    return minIndexByLength(idx_start + 1, cur_min_idx)

            return minIndexByLength(1, 0)

        def buildMappingFromWords(arr_words: List[str]):
            def iterateWords(i: int):
                if i > len(arr_words) - 1:
                    return
                recordSuffixIndex(arr_words[i], i)
                iterateWords(i + 1)

            iterateWords(0)

        buildMappingFromWords(wordsContainer)

        accumulator_result: List[int] = []

        def collectResults(iq: int):
            if iq > len(wordsQuery) - 1:
                return
            current_query = wordsQuery[iq]
            matched_idx = findOptimalIndex(current_query)
            accumulator_result.append(matched_idx)
            collectResults(iq + 1)

        collectResults(0)

        return accumulator_result