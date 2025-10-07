from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        map_suffixes: Dict[str, int] = {}

        def process_suffixes_at_index(currentPos: int, currentStr: str, outerIdx: int) -> None:
            if currentPos >= len(currentStr):
                return
            curr_sfx = currentStr[currentPos:]
            if curr_sfx not in map_suffixes:
                map_suffixes[curr_sfx] = outerIdx
            else:
                existing_idx = map_suffixes[curr_sfx]
                existing_word = wordsContainer[existing_idx]
                # Update if current word is shorter, or if equal length but smaller index
                if len(currentStr) < len(existing_word) or (len(currentStr) == len(existing_word) and outerIdx < existing_idx):
                    map_suffixes[curr_sfx] = outerIdx
            process_suffixes_at_index(currentPos + 1, currentStr, outerIdx)

        def iterate_words(idx: int) -> None:
            if idx >= len(wordsContainer):
                return
            process_suffixes_at_index(0, wordsContainer[idx], idx)
            iterate_words(idx + 1)

        iterate_words(0)

        def find_matching_index(QUERY: str) -> int:
            def iterate_query_pos(p: int) -> int:
                if p >= len(QUERY):
                    return -1
                candidate_sfx = QUERY[p:]
                if candidate_sfx in map_suffixes:
                    return map_suffixes[candidate_sfx]
                else:
                    return iterate_query_pos(p + 1)

            answer = iterate_query_pos(0)
            if answer != -1:
                return answer
            else:
                min_idx = 0
                min_len = len(wordsContainer[0])
                i = 1
                while i < len(wordsContainer):
                    current_len = len(wordsContainer[i])
                    if current_len < min_len or (current_len == min_len and i < min_idx):
                        min_len = current_len
                        min_idx = i
                    i += 1
                return min_idx

        outputs: List[int] = []

        def process_queries(j: int) -> None:
            if j >= len(wordsQuery):
                return
            idx_match = find_matching_index(wordsQuery[j])
            outputs.append(idx_match)
            process_queries(j + 1)

        process_queries(0)

        return outputs