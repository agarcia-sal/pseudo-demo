from math import inf
from functools import lru_cache

class Solution:
    def minimumCost(self, target, words, costs):
        mapping = {}
        idx = 0
        while idx < len(words):
            current_word = words[idx]
            current_cost = costs[idx]
            if current_word not in mapping or current_cost < mapping[current_word]:
                mapping[current_word] = current_cost
            idx += 1

        letters = []
        pos = 0
        while pos < len(target):
            letters.append(target[pos])
            pos += 1

        @lru_cache(None)
        def min_cost_to_form_target(position):
            if position == len(letters):
                return 0
            best_cost = inf
            pairs = list(mapping.items())
            i = 0
            while i < len(pairs):
                candidate_word, candidate_cost = pairs[i]
                word_len = len(candidate_word)
                if position + word_len <= len(letters):
                    matched = True
                    j = 0
                    while j < word_len and matched:
                        if letters[position + j] != candidate_word[j]:
                            matched = False
                        j += 1
                    if matched:
                        sub_cost = min_cost_to_form_target(position + word_len)
                        if sub_cost != inf:
                            combined_cost = candidate_cost + sub_cost
                            if combined_cost < best_cost:
                                best_cost = combined_cost
                i += 1
            return best_cost if best_cost != inf else inf

        answer = min_cost_to_form_target(0)
        return answer if answer != inf else -1