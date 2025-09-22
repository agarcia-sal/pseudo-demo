def main():
    # Step 1: Gather input
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of strings
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Step 3: Initialize a variable to count differences
    difference_count = 0
    
    # Step 4: Compare corresponding elements in both lists
    for index in range(3):  # Loop through the first three elements
        value_a = int(first_values[index])
        value_b = int(second_values[index])
        
        # Step 5: Check if the elements are different
        if value_a != value_b:
            difference_count += 1
    
    # Step 6: Determine the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function
main()


   1 2 3
   1 2 4
   

   5 6 7
   5 6 7
   

   10 20 30
   10 20 30
   

   1 2 3
   4 5 6
   

   0 0 0
   0 0 0
   