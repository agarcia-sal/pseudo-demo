class Solution:
    def getPermutationIndex(self, perm):
        length_of_perm = len(perm)
        modulus = (10**9) + 1

        factorials = [1] * length_of_perm
        iterator = 2
        while iterator < length_of_perm:
            factorials[iterator] = iterator * factorials[iterator - 1]
            iterator += 1

        available_numbers = list(range(1, length_of_perm + 1))

        result_index = 0
        position_index = 0
        while position_index < length_of_perm:
            current_element = perm[position_index]
            element_position = available_numbers.index(current_element)

            factorial_lookup_index = length_of_perm - position_index - 1
            product_value = element_position * factorials[factorial_lookup_index]
            result_index += product_value

            del available_numbers[element_position]
            position_index += 1

        return result_index % modulus