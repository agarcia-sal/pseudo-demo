class Solution:
    def maxNumber(self, num: int) -> int:
        result = 0
        if num == 1:
            result = 0
        else:
            self.bit_marker = 1
            self.findBit(self.bit_marker, num)
            bit_marker = self.bit_marker // 2
            interim = bit_marker - 1
            result = interim
        return result

    def findBit(self, current: int, threshold: int):
        if current <= threshold:
            self.bit_marker = current * 2
            self.findBit(self.bit_marker, threshold)