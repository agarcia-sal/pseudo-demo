class Solution:
    def minAnagramLength(self, s: str) -> int:
        def toBuildSet(string: str) -> set:
            res_set = set()
            idx = 0
            while idx < len(string):
                char_element = string[idx]
                if char_element not in res_set:
                    res_set.add(char_element)
                idx += 1
            return res_set

        counter = 0
        temporary_set = toBuildSet(s)
        iter_variable_list = list(temporary_set)
        while counter < len(iter_variable_list):
            counter += 1
        return counter