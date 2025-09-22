def adjust_quantity(quantity, divisor):
    # Calculate how many full groups can be made from the quantity
    full_groups = quantity // divisor
    remainder = quantity % divisor
    
    # If there is a remainder, adjust the result accordingly
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        return quantity  # No adjustment needed

def main():
    # Read a single line of input consisting of three integers n, m, s
    input_line = input()
    
    # Convert the input line into integers n, m, s
    n, m, s = map(int, input_line.split())
    
    # Adjust quantities using the adjust_quantity function
    adjusted_n = adjust_quantity(n, s)
    adjusted_m = adjust_quantity(m, s)
    
    # Calculate the product of adjusted quantities
    result = adjusted_n * adjusted_m
    
    # Print the resulting product
    print(result)

# Run the main program
if __name__ == "__main__":
    main()
