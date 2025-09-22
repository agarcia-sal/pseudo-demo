def main():
    # Read an integer input 'n'
    n = int(input())
    
    # Initialize a list 'b' of size 'n' with all values set to True
    b = [True] * n

    # Initialize variables
    j = 0  # Index for the list
    i = 1  # Incrementing value

    # Loop while 'i' is less than or equal to 500000
    while i <= 500000:
        # If current index 'j' in list 'b' is True
        if b[j]:
            b[j] = False  # Mark the index as False
        
        # Increment 'i' by 1
        i += 1
        
        # Update index 'j' using modulo to wrap around
        j = (j + i) % n

    # Filter out True values from list 'b'
    x = [a for a in b if a]  # List of elements in 'b' that are True

    # Check the length of the filtered list 'x'
    if len(x) == 0:
        print('YES')  # Output 'YES' if 'x' is empty
    else:
        print('NO')   # Output 'NO' if 'x' is not empty

if __name__ == "__main__":
    main()
