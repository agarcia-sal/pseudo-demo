def main():
    # Step 2: Input: Get an integer n from the user
    n = int(input())
    
    # Step 3: Initialize an array b of size n with all values set to True
    b = [True] * n

    # Step 4: Initialize index j to 0 and step i to 1
    j = 0
    i = 1

    # Step 5: While i is less than or equal to 500000 do:
    while i <= 500000:
        # a. If b[j] is True then:
        if b[j]:
            # i. Set b[j] to False
            b[j] = False
        # b. Increment i by 1
        i += 1
        # c. Update j to (j + i) modulo n
        j = (j + i) % n

    # Step 6: Create an array x to store elements from b that are still True
    x = [value for value in b if value]

    # Step 7: Check the size of x
    if len(x) == 0:
        # a. Output "YES"
        print("YES")
    else:
        # b. Output "NO"
        print("NO")

# Step 8: End of the program
if __name__ == "__main__":
    main()
