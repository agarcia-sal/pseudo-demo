def main():
    # Assume n is a positive integer input by the user
    n = int(input())
    
    # Initialize a list b with True values for each index from 0 to n-1
    b = [True] * n
    
    # Initialize counters
    j = 0
    i = 1

    # Loop while i is less than or equal to 500000
    while i <= 500000:
        # If the current index j in list b is True
        if b[j] is True:
            # Set the current index j in list b to False
            b[j] = False
        
        # Increment i by 1
        i += 1
        
        # Update j to the new index using modulo to keep it within bounds of n
        j = (j + i) % n
    
    # Create a new list x containing all elements in b that are still True
    x = [value for value in b if value]  # list comprehension to filter True values

    # Check the length of list x
    if len(x) == 0:
        print('YES')  # No True values remain in b
    else:
        print('NO')   # Some True values remain in b

# Entry point for the script
if __name__ == "__main__":
    main()
