class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        mapping = {}

        for w, c in zip(words, costs):
            if w not in mapping or c < mapping[w]:
                mapping[w] = c

        chars = list(target)

        from math import inf

        memo = {}

        def min_cost_to_form_target(index: int) -> int:
            if index == len(chars):
                return 0
            if index in memo:
                return memo[index]

            minimum = inf
            for entry_key, entry_val in mapping.items():
                length_word = len(entry_key)
                if index + length_word <= len(chars) and chars[index:index + length_word] == list(entry_key):
                    next_cost = min_cost_to_form_target(index + length_word)
                    if next_cost != inf:
                        cost = entry_val + next_cost
                        if cost < minimum:
                            minimum = cost

            memo[index] = minimum
            return minimum

        final = min_cost_to_form_target(0)
        if final != inf:
            return final
        else:
            return -1