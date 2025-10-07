from math import inf
from functools import lru_cache

class Solution:
    def minimumCost(self, target, words, costs):
        word_cost_map = {}
        for i in range(len(words)):
            word = words[i]
            cost = costs[i]
            if word not in word_cost_map or cost < word_cost_map[word]:
                word_cost_map[word] = cost

        target_chars = list(target)

        @lru_cache(None)
        def min_cost_to_form_target(idx):
            if idx >= len(target_chars):
                return 0

            min_cost = inf
            for word, cost in word_cost_map.items():
                length = len(word)
                if idx + length <= len(target_chars) and target_chars[idx:idx+length] == list(word):
                    next_cost = min_cost_to_form_target(idx + length)
                    if next_cost != inf:
                        candidate_cost = cost + next_cost
                        if candidate_cost < min_cost:
                            min_cost = candidate_cost

            return min_cost

        result = min_cost_to_form_target(0)
        return result if result != inf else -1