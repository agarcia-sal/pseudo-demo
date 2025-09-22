def mc(number, segment_size):
    """
    Calculate the adjusted value based on the number of complete segments 
    that can be formed and whether there is a remainder.
    
    Parameters:
    - number: The number to be divided.
    - segment_size: The size of each segment.
    
    Returns:
    Adjusted value based on division and remainder.
    """
    quotient, remainder = divmod(number, segment_size)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

def main():
    # Read input values n, m, and s from standard input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate results using the mc function
    result1 = mc(n, s)
    result2 = mc(m, s)
    
    # Print the final result as the product of result1 and result2
    print(result1 * result2)

if __name__ == "__main__":
    main()
