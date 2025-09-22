def do_main():
    # Step 1: Read inputs
    t1 = input()
    t2 = input()

    # Step 2: Split the inputs into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize a counter to track differences
    differences_count = 0

    # Step 4: Compare elements in both lists
    for x in range(3):  # Loop through the first three elements
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # If the elements are not equal, increment the counter
        if a != b:
            differences_count += 1

    # Step 5: Determine and output the result based on the counter
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Program Execution Start
do_main()
