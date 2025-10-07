class Solution:
    def clearStars(self, s: str) -> str:
        aux = []
        idx = 0
        while idx < len(s):
            curr = s[idx]
            if curr == "*":
                if aux:
                    aux.pop()
            else:
                aux.append(curr)
            idx += 1
        res_chars = ""
        pos = 0
        while pos < len(aux):
            res_chars += aux[pos]
            pos += 1
        return res_chars