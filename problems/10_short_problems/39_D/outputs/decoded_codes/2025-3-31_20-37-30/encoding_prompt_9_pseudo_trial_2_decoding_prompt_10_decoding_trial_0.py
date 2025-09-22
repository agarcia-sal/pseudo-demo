def compare_number_sets():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()

    # Step 3: Split Input Strings into Lists
    numbers_set1 = first_set.split()
    numbers_set2 = second_set.split()

    # Step 4: Initialize a Counter
    difference_count = 0

    # Step 5: Compare Each Position
    for index in range(3):  # We know there are exactly three positions
        num1 = int(numbers_set1[index])
        num2 = int(numbers_set2[index])
        
        if num1 != num2:
            difference_count += 1

    # Step 6: Output the Result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 1: Start Program
compare_number_sets()
