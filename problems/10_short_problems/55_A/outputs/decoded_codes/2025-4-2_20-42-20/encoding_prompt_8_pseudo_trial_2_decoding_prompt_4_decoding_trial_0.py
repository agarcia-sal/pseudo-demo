def mark_elements():
    # Step 1: Initialize Variables
    n = int(input())  # Read an integer value from user input
    b = [True] * n    # Create a list of size n filled with 'True'
    
    j = 0  # Index tracker for the list
    i = 1  # Steps taken

    # Step 2: Iterate to Mark Values
    while i <= 500000:
        # Check if the current index j in list b is 'True'
        if b[j]:
            b[j] = False  # Mark the value at index j as 'False'

        # Increment i by 1
        i += 1

        # Update index j using the formula and taking modulo n
        j = (j + i) % n

    # Step 3: Check Remaining True Values
    # Create a new list x that contains only 'True' values from list b
    x = [value for value in b if value]
    
    # Output the result based on the length of x
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the logic
mark_elements()
