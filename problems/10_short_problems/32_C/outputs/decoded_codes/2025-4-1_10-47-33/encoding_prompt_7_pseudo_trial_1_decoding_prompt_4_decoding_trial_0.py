def calculate_remainder_using_division(dividend, divisor):
    quotient, remainder = divmod(dividend, divisor)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

def main():
    quantity_a = int(input())
    quantity_b = int(input())
    size = int(input())
    
    result_a = calculate_remainder_using_division(quantity_a, size)
    result_b = calculate_remainder_using_division(quantity_b, size)
    
    final_result = result_a * result_b
    print(final_result)

if __name__ == "__main__":
    main()
