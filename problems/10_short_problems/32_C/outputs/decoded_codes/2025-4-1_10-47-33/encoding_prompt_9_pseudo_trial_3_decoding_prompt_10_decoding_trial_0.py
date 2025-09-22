def calculate_modified_value(number, divisor):
    # Calculate the quotient and remainder of the division
    quotient = number // divisor
    remainder = number % divisor
    
    # If there is a remainder, return the product of the remainder and (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    # If no remainder, return the original number
    else:
        return number

def main():
    # Read three integers from input
    value1 = int(input())
    value2 = int(input())
    divider = int(input())

    # Calculate modified values using the defined function
    modified_value1 = calculate_modified_value(value1, divider)
    modified_value2 = calculate_modified_value(value2, divider)

    # Calculate the product of modified values
    result = modified_value1 * modified_value2

    # Print the resulting product
    print(result)

if __name__ == "__main__":
    main()


  10
  20
  3
  

  7
  5
  2
  