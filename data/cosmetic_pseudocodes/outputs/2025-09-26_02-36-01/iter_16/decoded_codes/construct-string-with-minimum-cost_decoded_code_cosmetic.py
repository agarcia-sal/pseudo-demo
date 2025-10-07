class Solution:
    def minimumCost(self, target, words, costs):
        map_cost = {}
        idx_outer = 0
        while idx_outer < len(words):
            currentWord = words[idx_outer]
            currentCost = costs[idx_outer]
            if currentWord not in map_cost or currentCost < map_cost[currentWord]:
                map_cost[currentWord] = currentCost
            idx_outer += 1

        list_target = []
        idx_build = 0
        while idx_build < len(target):
            list_target.append(target[idx_build])
            idx_build += 1

        memo = {}
        INF = int(1e9) + 5

        def min_cost_to_form_target(zero_ind):
            if zero_ind == len(list_target):
                return 0
            if zero_ind in memo:
                return memo[zero_ind]

            smallest = INF
            for entry_word, entry_cost in map_cost.items():
                length_word = len(entry_word)
                if zero_ind + length_word <= len(list_target):
                    # slice_temp = list_target[zero_ind : zero_ind + length_word]
                    # list_word = list(entry_word)
                    matches = True
                    for idx_cmp in range(length_word):
                        if list_target[zero_ind + idx_cmp] != entry_word[idx_cmp]:
                            matches = False
                            break
                    if matches:
                        next_cost = min_cost_to_form_target(zero_ind + length_word)
                        if next_cost != INF:
                            proposed_cost = entry_cost + next_cost
                            if proposed_cost < smallest:
                                smallest = proposed_cost
            memo[zero_ind] = smallest if smallest != INF else INF
            return memo[zero_ind]

        computed_result = min_cost_to_form_target(0)
        if computed_result != INF:
            return computed_result
        else:
            return -1