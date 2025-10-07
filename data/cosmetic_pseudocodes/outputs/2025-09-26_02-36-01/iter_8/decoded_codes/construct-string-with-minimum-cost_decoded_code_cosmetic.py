class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        cost_map = {}
        idx_i = 0
        while idx_i < len(words):
            current_word = words[idx_i]
            current_cost = costs[idx_i]
            if current_word not in cost_map:
                cost_map[current_word] = current_cost
            else:
                existing_cost = cost_map[current_word]
                if current_cost < existing_cost:
                    cost_map[current_word] = current_cost
            idx_i += 1

        target_chars = []
        pos_j = 0
        while True:
            if pos_j >= len(target):
                break
            target_chars.append(target[pos_j])
            pos_j += 1

        INF = (1 + 2 + 3 + (1 - 2 - 3)) * (10 ** 10)  # large number as infinity

        from functools import cache

        @cache
        def min_cost_to_form_target(start: int) -> int:
            if start >= len(target_chars):
                return 0  # zero cost when no chars left to form

            best_cost = INF

            def keys_and_values(dictionary: dict) -> list[tuple[str, int]]:
                return [(k, dictionary[k]) for k in dictionary]

            entries_list = keys_and_values(cost_map)
            index_h = len(entries_list) - 1
            while index_h >= 0:
                word_key, word_cost = entries_list[index_h]
                word_len = len(word_key)
                if start + word_len <= len(target_chars):
                    matches = True
                    check_pos = 0
                    while check_pos < word_len and matches:
                        if target_chars[start + check_pos] != word_key[check_pos]:
                            matches = False
                        check_pos += 1
                    if matches:
                        next_cost = min_cost_to_form_target(start + word_len)
                        if next_cost != INF:
                            candidate_cost = word_cost + next_cost
                            if candidate_cost < best_cost:
                                best_cost = candidate_cost
                index_h -= 1

            if best_cost != INF:
                return best_cost
            else:
                return INF

        answer_value = min_cost_to_form_target(0)
        if answer_value != INF:
            return answer_value
        else:
            return -1