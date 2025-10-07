from math import inf
from functools import lru_cache

class Solution:
    def minimumCost(self, target, words, costs):
        mapping_cost = {}
        idx = 0
        n = len(words)
        while idx < n:
            current_word = words[idx]
            current_cost = costs[idx]
            if current_word not in mapping_cost:
                mapping_cost[current_word] = current_cost
            else:
                stored_cost = mapping_cost[current_word]
                if current_cost < stored_cost:
                    mapping_cost[current_word] = current_cost
            idx += 1

        target_chars = list(target)

        @lru_cache(None)
        def min_cost_to_form_target(start):
            if start == len(target_chars):
                return 0

            lowest_cost = inf
            for entry_key in mapping_cost:
                entry_value = mapping_cost[entry_key]
                segment_length = len(entry_key)
                end_pos = start + segment_length

                if end_pos <= len(target_chars):
                    segment_match = True
                    for char_pos in range(segment_length):
                        if target_chars[start + char_pos] != entry_key[char_pos]:
                            segment_match = False
                            break

                    if segment_match:
                        recursive_result = min_cost_to_form_target(end_pos)
                        if recursive_result != inf:
                            candidate_cost = entry_value + recursive_result
                            if candidate_cost < lowest_cost:
                                lowest_cost = candidate_cost

            return lowest_cost if lowest_cost != inf else inf

        final_answer = min_cost_to_form_target(0)
        return final_answer if final_answer != inf else -1