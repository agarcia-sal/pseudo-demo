def main():
    # Read an integer value 'n' from user input
    n = int(input())
    
    # Create a list 'b' of size n, initialized with True values
    b = [True] * n
    
    # Initialize index j and counter i
    j = 0
    i = 1

    # Loop that runs while i is less than or equal to 500000
    while i <= 500000:
        # Check if the current index j in list b is True
        if b[j]:
            # Set the current position in the list to False
            b[j] = False
            
        # Increment the counter i
        i += 1

        # Update index j using the given formula (we use modulo n to wrap around)
        j = (j + i) % n
    
    # Create a new list 'x' containing elements from b that are still True
    x = [value for value in b if value]

    # Check the length of list x
    if len(x) == 0:
        # If there are no True values left, print "YES"
        print('YES')
    else:
        # If there are still True values left, print "NO"
        print('NO')

# Entry point of the program
if __name__ == "__main__":
    main()
