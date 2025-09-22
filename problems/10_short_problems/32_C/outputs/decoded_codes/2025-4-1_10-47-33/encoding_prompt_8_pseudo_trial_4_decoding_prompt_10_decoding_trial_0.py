def adjust_quantity(quantity, divisor):
    """
    Calculate the adjusted quantity based on how many full groups can fit into the quantity.
    
    :param quantity: The original quantity (positive integer).
    :param divisor: The divisor used to determine full groups (positive integer).
    :return: The adjusted quantity based on remainder and full groups.
    """
    full_groups = quantity // divisor
    remainder = quantity % divisor
    
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        return quantity

def main():
    # Read a single line of input consisting of three integers
    input_line = input()
    
    # Split the input line into separate values and convert them to integers
    n, m, s = map(int, input_line.split())
    
    # Adjust the quantities n and m using the adjust_quantity function
    adjusted_n = adjust_quantity(n, s)
    adjusted_m = adjust_quantity(m, s)
    
    # Calculate the product of the adjusted values
    result = adjusted_n * adjusted_m
    
    # Print the resulting product
    print(result)

# Execute the main function
if __name__ == "__main__":
    main()
