from math import floor

def rounded_avg(integer_n: int, integer_m: int) -> str:
    var1_sum_accumulator: int = 0
    var2_counter: int = integer_n

    def loop_accumulate(value_acc: int, curr_index: int) -> int:
        if curr_index > integer_m:
            return value_acc
        return loop_accumulate(value_acc + curr_index, curr_index + 1)

    def is_less(a: int, b: int) -> bool:
        return a < b

    if not is_less(integer_m, integer_n):
        var1_sum_accumulator = loop_accumulate(var1_sum_accumulator, var2_counter)
        var3_count: int = (integer_m - integer_n) + 1
        var4_avg: float = var1_sum_accumulator / var3_count

        def round_to_int(input_float: float) -> int:
            varA_floor: int = floor(input_float)
            varB_frac: float = input_float - varA_floor
            return varA_floor + 1 if varB_frac >= 0.5 else varA_floor

        var5_rounded: int = round_to_int(var4_avg)

        def convert_to_binary(num: int) -> str:
            if num == 0:
                return "0"
            return convert_to_binary(num // 2) + str(num % 2)

        return convert_to_binary(var5_rounded)

    return "-1"