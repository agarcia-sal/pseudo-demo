def compare_number_sets():
    # Step 1: Receive two input strings
    first_set = input()
    second_set = input()
    
    # Step 2: Split both input strings into lists of numbers
    numbers_first = first_set.split()
    numbers_second = second_set.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Loop through each number in both lists
    for i in range(3):
        num_first = int(numbers_first[i])
        num_second = int(numbers_second[i])
        
        # Step 5: Check for differences
        if num_first != num_second:
            difference_count += 1
    
    # Step 6: Evaluate the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the function
compare_number_sets()


  1 2 3
  1 2 4
  

  5 6 7
  5 6 7
  

  10 20 30
  10 20 31
  

  1 2 3
  4 5 6
  