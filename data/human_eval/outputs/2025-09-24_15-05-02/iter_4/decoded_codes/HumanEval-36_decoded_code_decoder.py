def fizz_buzz(n: int) -> int:
    ns = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]
    concatenated_numbers = ''.join(str(num) for num in ns)
    ans = sum(1 for c in concatenated_numbers if c == '7')
    return ans