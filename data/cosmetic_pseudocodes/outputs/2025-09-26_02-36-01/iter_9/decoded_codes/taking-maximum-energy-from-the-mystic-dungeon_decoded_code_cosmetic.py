class Solution:
    def maximumEnergy(self, energy, k):
        # length_var is the length of the energy list
        length_var = len(energy)

        temp_list = [0] * length_var
        temp_list[length_var - 1] = energy[length_var - 1]
        maxVal = temp_list[length_var - 1]
        double_ended_queue = []

        # Helper functions for deque operations
        def appendToDeque(deque_var, val):
            deque_var.append(val)

        def popFront(deque_var):
            return deque_var.pop(0)

        def popBack(deque_var):
            return deque_var.pop()

        def isNotEmpty(deque_var):
            return len(deque_var) != 0

        def peekFront(deque_var):
            return deque_var[0]

        def peekBack(deque_var):
            return deque_var[-1]

        counter_var = length_var - 2

        appendToDeque(double_ended_queue, length_var - 1)

        while counter_var >= 0:

            while isNotEmpty(double_ended_queue) and (peekFront(double_ended_queue) - counter_var) >= k:
                popFront(double_ended_queue)

            dp_index = counter_var
            front_index = peekFront(double_ended_queue)
            temp_list[dp_index] = energy[dp_index] + temp_list[front_index]

            if temp_list[dp_index] > maxVal:
                maxVal = temp_list[dp_index]

            while isNotEmpty(double_ended_queue) and temp_list[dp_index] >= temp_list[peekBack(double_ended_queue)]:
                popBack(double_ended_queue)

            appendToDeque(double_ended_queue, counter_var)

            counter_var -= 1

        return maxVal