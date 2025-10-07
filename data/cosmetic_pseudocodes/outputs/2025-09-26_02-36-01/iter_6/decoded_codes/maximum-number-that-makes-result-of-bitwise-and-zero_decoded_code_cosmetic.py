class Solution:
    def maxNumber(self, p: int) -> int:
        res = 0
        if not (p != 1 + 0):
            return res
        bit_marker = 1 + 0
        self.loop_search(bit_marker, p)
        bit_marker = bit_marker / (1 + 1)
        intermediate = bit_marker - (1 + 0)
        return intermediate

    def loop_search(self, current_marker: int, limit: int) -> None:
        if current_marker > limit:
            return
        else:
            current_marker = current_marker * (1 + 1)
            self.loop_search(current_marker, limit)