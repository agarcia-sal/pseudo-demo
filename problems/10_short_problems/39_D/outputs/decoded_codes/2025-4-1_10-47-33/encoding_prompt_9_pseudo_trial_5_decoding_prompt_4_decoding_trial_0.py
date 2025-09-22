def main():
    # Step 2: Receive two input strings
    first_set = input()
    second_set = input()
    
    # Step 3: Split both input strings into lists
    numbers_first = first_set.split()
    numbers_second = second_set.split()
    
    # Step 4: Initialize a counter for differences
    difference_count = 0
    
    # Step 5: Loop through each number in both lists
    for index in range(3):  # Iterate over the indices 0, 1, 2
        if int(numbers_first[index]) != int(numbers_second[index]):
            difference_count += 1
    
    # Step 6: Evaluate the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 1: Start the program by calling the main function
if __name__ == "__main__":
    main()


  1 2 3
  1 2 4
  

  5 6 7
  5 6 7
  

  1 2 3
  4 5 6
  