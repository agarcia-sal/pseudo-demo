def do_main():
    # Step 1: Get input from the user
    input1 = input()
    input2 = input()
    
    # Step 2: Split input strings into lists
    list1 = input1.split()
    list2 = input2.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0 
    
    # Step 4: Compare corresponding elements from both lists
    for index in range(3):
        # Convert to integers
        num1 = int(list1[index])
        num2 = int(list2[index])
        
        # Check if the elements are different
        if num1 != num2:
            difference_count += 1 
            
    # Step 5: Determine the outcome based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution
do_main()
