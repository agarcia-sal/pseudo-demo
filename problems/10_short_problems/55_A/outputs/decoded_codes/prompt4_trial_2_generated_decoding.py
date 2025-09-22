def main():
    # Read an integer input which represents the size of the array
    n = int(input())

    # Initialize an array of boolean values, all set to True
    b = [True] * n

    # Initialize index variables
    j = 0
    i = 1

    # Loop until variable i exceeds 500,000
    while i <= 500000:
        # If the current index in array b is True
        if b[j]:
            # Set the current index in array b to False
            b[j] = False

        # Increment i by 1
        i += 1

        # Update j to the next index in a circular manner using modulus
        j = (j + i) % n

    # Create a new list containing only the True values from array b
    x = [value for value in b if value]

    # Check if the list x is empty
    if len(x) == 0:
        # If empty, print 'YES'
        print('YES')
    else:
        # If not empty, print 'NO'
        print('NO')

# Execute the main function
if __name__ == "__main__":
    main()
