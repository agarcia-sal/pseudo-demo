def main():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()

    # Step 3: Split Input into Lists
    first_list = first_set.split()
    second_list = second_set.split()

    # Step 4: Initialize a Counter
    difference_count = 0

    # Step 5: Compare Corresponding Values
    for index in range(3):  # Since we are only dealing with 3 values
        value_from_first = int(first_list[index])
        value_from_second = int(second_list[index])
        
        if value_from_first != value_from_second:
            difference_count += 1

    # Step 6: Evaluate the Result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the main process
if __name__ == "__main__":
    main()


  1 2 3
  1 2 3
  

  1 2 3
  1 2 4
  

  1 2 3
  0 2 4
  

  1 2 3
  4 5 6
  