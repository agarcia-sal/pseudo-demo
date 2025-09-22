def main():
    # Step 1: Initialize variable
    n = int(input())  # Read input and convert to integer

    # Step 2: Create a list 'b' of Boolean values initialized to True
    b = [True] * n

    # Step 3: Initialize counters
    j = 0
    i = 1

    # Step 4: Loop while 'i' is less than or equal to 500000
    while i <= 500000:
        # Step 5: Check if the current position 'j' is still True
        if b[j]:
            b[j] = False  # Mark the position as False

        # Increment 'i' and update 'j' for the next iteration
        i += 1
        j = (j + i) % n  # Update 'j' using modular arithmetic

    # Step 6: Create list 'x' to store positions in 'b' that are still True
    x = [index for index, value in enumerate(b) if value]

    # Step 7: Check the length of 'x'
    if len(x) == 0:
        print('YES')  # All values have been marked False
    else:
        print('NO')  # There are still True values in 'b'

if __name__ == "__main__":
    main()
