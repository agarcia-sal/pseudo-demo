def process_input():
    # Step 1: Read an integer from user input
    n = int(input())
    
    # Step 2: Initialize a list 'b' with 'n' elements, all set to True
    b = [True] * n

    # Step 3: Initialize variables
    j = 0  # Current index in the list
    i = 1  # Step counter

    # Step 4: Loop until i exceeds 500000
    while i <= 500000:
        # Step 5: Check if the current index in list 'b' is True
        if b[j]:
            # Step 6: Set the current index to False
            b[j] = False

        # Step 7: Increment i by 1
        i += 1

        # Step 8: Update j to wrap around within bounds of 'n'
        j = (j + i) % n

    # Step 9: Create a list 'x' of elements in 'b' that are still True
    x = [elem for elem in b if elem]

    # Step 10: Check the length of list 'x'
    if len(x) == 0:
        print('YES')
    else:
        print('NO')

# To execute the function
process_input()
