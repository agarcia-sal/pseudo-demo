from typing import List, Dict

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        sigma: Dict[str, int] = {}

        for h, current_word in enumerate(wordsContainer):
            length_current = len(current_word)
            for p in range(length_current):
                current_suffix = current_word[p:]
                if current_suffix not in sigma:
                    sigma[current_suffix] = h
                else:
                    existing_idx = sigma[current_suffix]
                    existing_word = wordsContainer[existing_idx]
                    if (len(current_word) < len(existing_word)) or (len(current_word) == len(existing_word) and h < existing_idx):
                        sigma[current_suffix] = h

        def get_best_match(query: str) -> int:
            u = 0
            length_query = len(query)
            while u < length_query:
                trial_suffix = query[u:]
                if trial_suffix in sigma:
                    return sigma[trial_suffix]
                u += 1

            # If no suffix found, return index of shortest word; if tie lowest index
            min_idx_candidate = 0
            for v in range(1, len(wordsContainer)):
                if (len(wordsContainer[v]) < len(wordsContainer[min_idx_candidate])) or (
                    len(wordsContainer[v]) == len(wordsContainer[min_idx_candidate]) and v < min_idx_candidate):
                    min_idx_candidate = v
            return min_idx_candidate

        output_array = []
        for w in wordsQuery:
            output_array.append(get_best_match(w))

        return output_array