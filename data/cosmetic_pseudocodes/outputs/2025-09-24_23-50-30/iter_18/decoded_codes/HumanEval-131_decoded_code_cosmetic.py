from typing import Callable

def digits(lambda_: int) -> int:
    def helper(index_lambda: int, acc_product: int, acc_count: int) -> int:
        if index_lambda == len(str(lambda_)):
            return 0 if acc_count == 0 else acc_product

        ch = str(lambda_)[index_lambda]
        num = int(ch)
        if (num // 2) * 2 == num:
            return helper(index_lambda + 1, acc_product, acc_count)
        return helper(index_lambda + 1, acc_product * num, acc_count + 1)

    return helper(0, 1, 0)