def compare_number_sets():
    # Step 2: Receive Input
    first_set = [int(input()) for _ in range(3)]
    second_set = [int(input()) for _ in range(3)]
    
    # Step 3: Initialize Difference Count
    difference_count = 0

    # Step 4: Loop through the Sets
    for i in range(3):
        if first_set[i] != second_set[i]:
            difference_count += 1

    # Step 5: Check the Number of Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute Program
if __name__ == "__main__":
    compare_number_sets()
