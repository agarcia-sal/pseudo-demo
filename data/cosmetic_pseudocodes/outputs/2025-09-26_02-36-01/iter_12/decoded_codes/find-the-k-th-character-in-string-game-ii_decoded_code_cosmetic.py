class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        def half_value(v: int) -> int:
            return v // 2

        def is_equal(a: int, b: int) -> bool:
            return a == b

        def shift_char(c: str) -> str:
            base_ascii = 97
            offset = ord(c) - base_ascii
            new_offset = (offset + 1) % 26
            return chr(base_ascii + new_offset)

        acc_length = 1
        ops_store = []

        def append_op(val: int):
            nonlocal acc_length
            ops_store.append(val)
            acc_length *= 2

        for op in param_operations:
            append_op(op)

        res_char = "a"
        pos = len(ops_store) - 1

        while pos >= 0:
            half_len = half_value(acc_length)
            if param_k > half_len:
                param_k -= half_len
                acc_length = half_len
                if is_equal(ops_store[pos], 1):
                    res_char = shift_char(res_char)
            else:
                acc_length = half_len
            pos -= 1

        return res_char