class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        cost_map = {}
        idx1 = 0
        while idx1 < len(words):
            w = words[idx1]
            c = costs[idx1]
            if w not in cost_map:
                cost_map[w] = c
            else:
                if c < cost_map[w]:
                    cost_map[w] = c
            idx1 += 1

        chars = list(target)
        n = len(chars)
        INF = float('inf')
        memo = {}

        def min_cost_to_form_target(pos: int) -> int:
            if pos == n:
                return 0
            if pos in memo:
                return memo[pos]

            best_cost = INF
            iter_pairs = list(cost_map.items())
            i = 0

            while i < len(iter_pairs):
                word, price = iter_pairs[i]
                word_len = len(word)
                if pos + word_len <= n:
                    slice_chars = []
                    j = 0
                    while j < word_len:
                        slice_chars.append(chars[pos + j])
                        j += 1

                    match_flag = True
                    k = 0
                    while k < word_len and match_flag:
                        if slice_chars[k] != word[k]:
                            match_flag = False
                        k += 1

                    if match_flag:
                        candidate_cost = min_cost_to_form_target(pos + word_len)
                        if candidate_cost != INF:
                            total_cost = candidate_cost + price
                            if total_cost < best_cost:
                                best_cost = total_cost
                i += 1

            memo[pos] = best_cost if best_cost != INF else INF
            return memo[pos]

        answer = min_cost_to_form_target(0)
        return answer if answer != INF else -1