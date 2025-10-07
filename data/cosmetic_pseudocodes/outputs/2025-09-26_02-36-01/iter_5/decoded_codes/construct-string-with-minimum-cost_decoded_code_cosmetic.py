class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        cost_lookup = {}

        def build_cost_map(index: int) -> None:
            if index >= len(words):
                return
            current_word = words[index]
            current_cost = costs[index]
            if current_word not in cost_lookup:
                cost_lookup[current_word] = current_cost
            else:
                if current_cost < cost_lookup[current_word]:
                    cost_lookup[current_word] = current_cost
            build_cost_map(index + 1)

        build_cost_map(0)

        array_of_chars = list(target)

        from math import inf

        def compute_min_cost(position: int) -> float:
            if position == len(array_of_chars):
                return 0  # base case: full coverage

            minimum_found = inf
            helper_keys = list(cost_lookup.keys())
            helper_values = list(cost_lookup.values())

            def iterate_over_words(i: int, current_min: float) -> float:
                if i >= len(helper_keys):
                    return current_min

                candidate_word = helper_keys[i]
                candidate_cost = helper_values[i]
                word_len = len(candidate_word)
                boundary = position + word_len
                if boundary <= len(array_of_chars):
                    segment = array_of_chars[position:boundary]
                    candidate_chars = list(candidate_word)
                    matches = True
                    idx = 0
                    while matches and idx < word_len:
                        if segment[idx] != candidate_chars[idx]:
                            matches = False
                        idx += 1
                    if matches:
                        cost_subproblem = compute_min_cost(boundary)
                        if cost_subproblem != inf:
                            combined_cost = candidate_cost + cost_subproblem
                            if combined_cost < current_min:
                                current_min = combined_cost
                return iterate_over_words(i + 1, current_min)

            minimum_found = iterate_over_words(0, minimum_found)
            return minimum_found

        answer = compute_min_cost(0)

        if answer != float('inf'):
            return answer
        return -1