def mc(number, segment_size):
    """
    Calculate the adjusted value based on how many complete segments can
    be formed and whether there is a remainder.
    
    Parameters:
    number (int): The number to be segmented
    segment_size (int): The size of each segment
    
    Returns:
    int: Adjusted value based on segments
    """
    quotient, remainder = divmod(number, segment_size)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

def main():
    # Read input values from standard input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate results using the mc function
    result1 = mc(n, s)
    result2 = mc(m, s)
    
    # Print the final product of the two results
    print(result1 * result2)

# Execute the main function to run the code
if __name__ == "__main__":
    main()
