def main():
    # Read input value for n
    n = int(input())
    
    # Initialize a list of boolean values, all set to True
    boolean_list = [True] * n
    
    # Initialize control variables
    j = 0
    i = 1
    
    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current position in the list is True
        if boolean_list[j]:
            # Mark the position as False
            boolean_list[j] = False
        
        # Increment i
        i += 1
        
        # Update the index j in a circular manner
        j = (j + i) % n
    
    # Create a list of True values from boolean_list
    true_values = [v for v in boolean_list if v]
    
    # Check if there are any True values remaining
    if len(true_values) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
