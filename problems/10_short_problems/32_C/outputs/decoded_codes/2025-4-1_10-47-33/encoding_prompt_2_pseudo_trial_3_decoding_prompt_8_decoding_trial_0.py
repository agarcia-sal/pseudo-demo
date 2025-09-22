def mc(number, divisor):
    q = number // divisor
    r = number % divisor
    if r > 0:
        return r * (q + 1)
    else:
        return number

# Input Section
total1, total2, divisor = map(int, input().split())

# Processing Section
result1 = mc(total1, divisor)
result2 = mc(total2, divisor)

# Output Section
final_product = result1 * result2
print(final_product)
