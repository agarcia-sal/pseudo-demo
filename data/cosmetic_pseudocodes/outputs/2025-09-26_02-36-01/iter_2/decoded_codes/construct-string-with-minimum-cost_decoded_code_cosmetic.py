class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        cost_map = {}
        idx = 0
        while idx < len(words):
            current_word = words[idx]
            current_cost = costs[idx]
            if current_word not in cost_map:
                cost_map[current_word] = current_cost
            else:
                if cost_map[current_word] > current_cost:
                    cost_map[current_word] = current_cost
            idx += 1

        tgt_chars = [ch for ch in target]

        from math import inf
        from functools import lru_cache

        @lru_cache(None)
        def min_cost_to_form_target(position: int) -> int:
            if position == len(tgt_chars):
                return 0

            minimum_val = inf

            for word_str, word_cost_val in cost_map.items():
                word_len = len(word_str)
                if position + word_len <= len(tgt_chars):
                    segment = tgt_chars[position : position + word_len]
                    word_array = [ch for ch in word_str]

                    if segment == word_array:
                        recursive_cost = min_cost_to_form_target(position + word_len)
                        if recursive_cost != inf:
                            total_cost = word_cost_val + recursive_cost
                            if total_cost < minimum_val:
                                minimum_val = total_cost

            if minimum_val != inf:
                return minimum_val
            else:
                return inf

        answer = min_cost_to_form_target(0)
        return answer if answer != inf else -1