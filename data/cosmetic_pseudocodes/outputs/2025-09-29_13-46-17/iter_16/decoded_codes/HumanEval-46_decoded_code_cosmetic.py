from typing import List


def fib4(integer_n: int) -> int:
    ϟ𝛞𝛴χl: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return ϟ𝛞𝛴χl[integer_n]
    else:
        つ𓀈: int = 4
        while つ𓀈 <= integer_n:
            λΡϮδ𝗇: int = 0
            ρɓ𐂂ⅾ: int = 1
            ȡдન: int = len(ϟ𝛞𝛴χl)
            while ρɓ𐂂ⅾ <= 4:
                λΡϮδ𝗇 += ϟ𝛞𝛴χl[ȡдન - ρɓ𐂂ⅾ]
                ρɓ𐂂ⅾ += 1
            ϟ𝛞𝛴χl.append(λΡϮδ𝗇)
            𝓦𐰭: List[int] = ϟ𝛞𝛴χl[1:]
            ϟ𝛞𝛴χl = 𝓦𐰭
            つ𓀈 += 1
        return ϟ𝛞𝛴χl[-1]