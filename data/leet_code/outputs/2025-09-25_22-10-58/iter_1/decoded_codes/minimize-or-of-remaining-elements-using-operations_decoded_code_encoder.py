from typing import List

class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        def canAchieve(target_or: int) -> bool:
            current_and = -1
            operations = 0
            for num in nums:
                if current_and == -1:
                    current_and = num
                else:
                    current_and &= num
                # If current_and & target_or == 0, reset current_and, else increment operations
                if (current_and & target_or) == 0:
                    current_and = -1
                else:
                    operations += 1
                    if operations > k:
                        return False
            return True

        max_possible_value = (1 << 30) - 1
        result = max_possible_value
        for bit in range(30):
            bit_mask = 1 << bit
            if (result & bit_mask) == 0:
                continue
            # Logical NOT in Python for bitwise means flipping bits with ~. Careful with 30 bits.
            # We want to flip bit_mask in result, so ~(bit_mask) & max_possible_value to keep within 30 bits
            # Then target_or is (~result ^ bit_mask) & max_possible_value
            # But in pseudocode it says logical NOT of result XOR bit_mask. 
            # Actually the pseudocode says "IF canAchieve(LOGICAL NOT OF result XOR bit_mask k)"
            # So logical NOT OF (result XOR bit_mask) means invert all bits of (result XOR bit_mask) within 30 bits
            candidate = ~(result ^ bit_mask) & max_possible_value
            if canAchieve(candidate):
                result &= ~bit_mask & max_possible_value
        return result