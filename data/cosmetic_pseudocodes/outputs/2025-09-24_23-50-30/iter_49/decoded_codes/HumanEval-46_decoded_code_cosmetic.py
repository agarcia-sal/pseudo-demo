from typing import List

def fib4(integer_alpha: int) -> int:
    def sumNewestFour(return_list: List[int], index_pointer: int) -> int:
        return (
            return_list[index_pointer - 1]
            + return_list[index_pointer - 2]
            + return_list[index_pointer - 3]
            + return_list[index_pointer - 4]
        )

    stockpile: List[int] = [0, 0, 2, 0]

    if integer_alpha < 4:
        return stockpile[integer_alpha]
    else:
        def recurseDelta(current_step: int, max_limit: int, buffer: List[int]) -> int:
            if current_step > max_limit:
                return buffer[3]
            sum_of_quadruple = sumNewestFour(buffer, 4)
            buffer.pop(0)
            buffer.append(sum_of_quadruple)
            return recurseDelta(current_step + 1, max_limit, buffer)

        return recurseDelta(4, integer_alpha, stockpile)