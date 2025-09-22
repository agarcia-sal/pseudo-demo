def main():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()

    # Step 3: Split Input into Individual Numbers
    first_list = first_set.split()
    second_list = second_set.split()

    # Step 4: Initialize a Counter for Differences
    difference_count = 0

    # Step 5: Compare Each Number in the Sets
    for index in range(3):
        first_number = int(first_list[index])
        second_number = int(second_list[index])

        if first_number != second_number:
            difference_count += 1

    # Step 6: Determine the Result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 1: Start the Program
if __name__ == "__main__":
    main()


   1 2 3
   1 2 4
   

   5 6 7
   5 6 8
   

   9 8 7
   9 1 7
   

   1 2 3
   4 5 6
   