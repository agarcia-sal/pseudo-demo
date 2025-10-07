from typing import Callable

def digitSum(string_input: str) -> int:
    def Υ53_β(s: str, acc: int) -> int:
        if s == "":
            return acc
        ϖψ = s[0]
        ϯ₧ = ('A' <= ϖψ <= 'Z')
        Ω₤ = (ord(ϖψ) if ϯ₧ else 0)
        return Υ53_β(s[1:], acc + Ω₤)
    return Υ53_β(string_input, 0)