class Solution:
    def maximumEnergy(self, energy, k):
        length_energy = len(energy)

        dynamic_array = [0] * length_energy
        dynamic_array[-1] = energy[-1]

        peak_energy = dynamic_array[-1]

        def front_value(dq):
            return dq[0]

        def back_value(dq):
            return dq[-1]

        def pop_front(dq):
            return dq[1:]

        def pop_back(dq):
            return dq[:-1]

        indices_deque = [length_energy - 1]

        def process_index(position, dp_state, indices_state, current_max):
            if position < 0:
                return current_max

            # Remove indices from front where distance >= k
            while indices_state and front_value(indices_state) - position >= k:
                indices_state = pop_front(indices_state)

            reference_index = front_value(indices_state)
            computed_value = energy[position] + dp_state[reference_index]
            dp_state[position] = computed_value

            updated_max = current_max
            if updated_max < computed_value:
                updated_max = computed_value

            # Maintain decreasing dp values in indices_state
            while indices_state and dp_state[position] >= dp_state[back_value(indices_state)]:
                indices_state = pop_back(indices_state)

            indices_state.append(position)

            return process_index(position - 1, dp_state, indices_state, updated_max)

        final_result = process_index(length_energy - 2, dynamic_array, indices_deque, peak_energy)

        return final_result