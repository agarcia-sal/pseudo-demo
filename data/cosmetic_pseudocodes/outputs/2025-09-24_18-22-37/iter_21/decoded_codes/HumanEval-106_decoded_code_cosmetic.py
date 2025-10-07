from typing import List

def f(input_param: int) -> List[int]:
    output_seq: List[int] = []
    counter: int = 1
    while counter <= input_param:
        if (counter % 2) == 0:
            prod_accumulator: int = 1
            for multiplier in range(1, counter + 1):
                prod_accumulator *= multiplier
            output_seq.append(prod_accumulator)
        else:
            sum_accumulator: int = 0
            iterator: int = 1
            while iterator <= counter:
                sum_accumulator += iterator
                iterator += 1
            output_seq.append(sum_accumulator)
        counter += 1
    return output_seq