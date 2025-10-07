from math import inf

class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        word_cost_dict = {}
        for word, cost in zip(words, costs):
            if word not in word_cost_dict or cost < word_cost_dict[word]:
                word_cost_dict[word] = cost

        target_list = list(target)
        memo = {}

        def min_cost_to_form_target(start: int) -> int:
            if start == len(target_list):
                return 0
            if start in memo:
                return memo[start]

            min_cost = inf
            for word, cost in word_cost_dict.items():
                length = len(word)
                if start + length <= len(target_list):
                    if target_list[start:start+length] == list(word):
                        cost_to_complete = min_cost_to_form_target(start + length)
                        if cost_to_complete != inf:
                            current_cost = cost + cost_to_complete
                            if current_cost < min_cost:
                                min_cost = current_cost
            memo[start] = min_cost
            return min_cost

        result = min_cost_to_form_target(0)
        return result if result != inf else -1