def main():
    # Step 2: Read input value for n
    n = int(input())
    
    # Step 4: Create a boolean list b of size n, initializing all elements to True
    b = [True] * n
    
    # Step 5 and 6: Initialize integer variables j and i
    j = 0
    i = 1

    # Step 7: Loop until i exceeds 500000
    while i <= 500000:
        # Step 7a: If b[j] is True, set it to False
        if b[j]:
            b[j] = False
        
        # Step 7b: Increment i by 1
        i += 1
        
        # Step 7c: Update j using modulo operation
        j = (j + i) % n

    # Step 8: Create a new list x containing all True elements from b
    x = [value for value in b if value]

    # Step 9: Check the length of x for final output
    if len(x) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
