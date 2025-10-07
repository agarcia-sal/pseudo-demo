class Solution:
    def minimumLevels(self, possible):
        accumulated_total = 0
        iterator_idx = 0
        while iterator_idx < len(possible):
            current_val = possible[iterator_idx]
            increment_val = (current_val * 2) - 1
            accumulated_total += increment_val
            iterator_idx += 1

        alice_score = 0
        position_counter = 0

        def check_position(possible_list, pos, running_alice, running_total):
            if not (pos < len(possible_list) - 1):
                return -1

            current_element = possible_list[pos]
            alice_addition = (current_element * 2) - 1
            new_alice = running_alice + alice_addition
            total_subtraction = (current_element * 2) - 1
            new_total = running_total - total_subtraction

            if new_alice > new_total:
                return pos + 1
            else:
                return check_position(possible_list, pos + 1, new_alice, new_total)

        result = check_position(possible, position_counter, alice_score, accumulated_total)
        return result