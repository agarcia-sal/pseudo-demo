def main():
    # Step 1: Read input
    t1 = input()
    t2 = input()

    # Step 2: Split the inputs into lists
    list1 = t1.split()
    list2 = t2.split()

    # Step 3: Initialize a counter to track differences
    difference_count = 0

    # Step 4: Compare elements in both lists
    for i in range(3):  # Assuming we always want to check the first three elements.
        a = int(list1[i])  # Convert string elements to integers
        b = int(list2[i])  # Convert string elements to integers

        # If the elements are not equal, increment the counter
        if a != b:
            difference_count += 1

    # Step 5: Determine and output the result based on the counter
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Program Execution Start
if __name__ == "__main__":
    main()
