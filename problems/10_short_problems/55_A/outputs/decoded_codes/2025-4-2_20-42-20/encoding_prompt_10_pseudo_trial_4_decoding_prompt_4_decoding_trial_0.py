def main():
    # Step 1: Input the number n
    n = int(input())

    # Step 2: Initialize a list b with TRUE values
    b = [True] * n

    # Step 3: Initialize loop control variables
    j = 0
    i = 1

    # Step 4: Main loop to update the list b
    while i <= 500000:
        # Step 5: Check if current position j is marked TRUE
        if b[j]:
            b[j] = False
        
        # Step 6: Increment i and update j for the next iteration
        i += 1
        j = (j + i) % n

    # Step 7: Create a list x with all TRUE values from list b
    x = [value for value in b if value]

    # Step 8: Check if list x is empty
    if len(x) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
