def main():
    # Receive Input
    first_set = [int(x) for x in input().split()]
    second_set = [int(x) for x in input().split()]

    # Initialize Difference Count
    difference_count = 0

    # Loop through the Sets
    for i in range(3):
        if first_set[i] != second_set[i]:
            difference_count += 1

    # Check the Number of Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execution of Program
if __name__ == "__main__":
    main()


  1 2 3
  1 2 4
  

  1 2 3
  4 5 6
  