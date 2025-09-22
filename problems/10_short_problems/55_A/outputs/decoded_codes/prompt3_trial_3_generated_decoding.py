def main():
    n = int(input())  # Input the integer value 'n'

    # Create a list 'b' of size 'n' and initialize all elements to True
    b = [True] * n  

    j = 0  # Tracker for the current index in list
    i = 1  # Step counter

    # Loop until 'i' exceeds 500000
    while i <= 500000:
        # Check if the current index j in list b is still marked True
        if b[j]:
            b[j] = False  # Mark the current index as False

        i += 1  # Increment i by 1
        j = (j + i) % n  # Update j to move forward by i steps and wrap around using modulo n

    # Create a new list 'x' containing only the True values from 'b'
    x = [value for value in b if value]  

    # Check the length of the list 'x'
    if len(x) == 0:
        print('YES')  # All elements have been marked False
    else:
        print('NO')   # There are still True elements in the list

# Call the main function
if __name__ == "__main__":
    main()
