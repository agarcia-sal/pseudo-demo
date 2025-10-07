import math

class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        cost_mapping = {}
        total_words = len(words)
        idx = 0
        while idx < total_words:
            current_word = words[idx]
            current_cost = costs[idx]
            if current_word not in cost_mapping or current_cost < cost_mapping[current_word]:
                cost_mapping[current_word] = current_cost
            idx += 1

        target_chars = list(target)
        target_len = len(target_chars)
        memo = {}

        def min_cost_to_form_target(position: int) -> int:
            if position == target_len:
                return 0
            if position in memo:
                return memo[position]

            minimal_cost = math.inf
            for dict_word, dict_cost in cost_mapping.items():
                dict_word_length = len(dict_word)
                next_pos = position + dict_word_length
                if next_pos <= target_len:
                    target_segment = target_chars[position:next_pos]
                    dict_word_chars = list(dict_word)
                    # Check if target segment matches dict_word characters
                    if all(target_segment[i] == dict_word_chars[i] for i in range(dict_word_length)):
                        next_cost = min_cost_to_form_target(next_pos)
                        if next_cost != math.inf:
                            combined_cost = dict_cost + next_cost
                            if combined_cost < minimal_cost:
                                minimal_cost = combined_cost

            memo[position] = minimal_cost
            return minimal_cost

        final_cost = min_cost_to_form_target(0)
        return final_cost if final_cost != math.inf else -1