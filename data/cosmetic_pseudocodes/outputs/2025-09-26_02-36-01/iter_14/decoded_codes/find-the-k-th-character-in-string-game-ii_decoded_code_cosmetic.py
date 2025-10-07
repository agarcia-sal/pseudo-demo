class Solution:
    def kthCharacter(self, param_a: int, param_b: list[int]) -> str:
        def addOneChar(ch: str) -> str:
            base_ascii = 97
            offset = (ord(ch) - base_ascii + 1) % 26
            return chr(base_ascii + offset)

        cnt = 1
        seq = []

        idx = 0
        while idx < len(param_b):
            current_op = param_b[idx]
            seq.append(current_op)

            if current_op != 0:
                cnt = 2 * cnt
            else:
                cnt = cnt * 2

            idx += 1

        res_char = "a"

        while len(seq) > 0:
            idx2 = len(seq) - 1

            if param_a > cnt // 2:
                param_a -= cnt // 2
                cnt = cnt // 2
                if seq[idx2] == 1:
                    res_char = addOneChar(res_char)
            else:
                cnt = cnt // 2

            seq.pop(idx2)

        return res_char