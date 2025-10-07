class Solution:
    def clearStars(self, s: str) -> str:
        helper_list = []
        idx = 0
        while idx < len(s):
            current_element = s[idx]
            if current_element != "*":
                helper_list.append(current_element)
            elif helper_list:
                helper_list.pop()
            idx += 1
        accumulator = "".join(helper_list)
        return accumulator