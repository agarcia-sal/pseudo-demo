class Solution:
    def minimumCost(self, target, words, costs):
        cost_map = {}
        for i in range(len(words)):
            w = words[i]
            c = costs[i]
            if w in cost_map:
                if c < cost_map[w]:
                    cost_map[w] = c
            else:
                cost_map[w] = c

        chars = list(target)

        from math import inf

        memo = {}

        def min_cost_to_form_target(pos):
            if pos == len(chars):
                return 0
            if pos in memo:
                return memo[pos]

            best_cost = inf
            for key, val in cost_map.items():
                wlen = len(key)
                if pos + wlen <= len(chars):
                    segment = chars[pos:pos + wlen]
                    if segment == list(key):
                        rest_cost = min_cost_to_form_target(pos + wlen)
                        if rest_cost != inf:
                            total = val + rest_cost
                            if total < best_cost:
                                best_cost = total

            memo[pos] = best_cost
            return best_cost

        answer = min_cost_to_form_target(0)
        if answer == inf:
            return -1
        else:
            return answer