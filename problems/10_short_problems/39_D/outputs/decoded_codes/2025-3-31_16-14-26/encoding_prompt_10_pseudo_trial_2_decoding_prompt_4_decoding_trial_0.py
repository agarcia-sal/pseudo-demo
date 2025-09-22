def do_main():
    # Step 1: Get input from the user
    t1 = input()
    t2 = input()
    
    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split the first input string by whitespace
    tt2 = t2.split()  # Split the second input string by whitespace
    
    # Step 3: Initialize a counter for differences
    differences_count = 0 
    
    # Step 4: Compare corresponding elements from both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Check if the elements are different
        if a != b:
            differences_count += 1
            
    # Step 5: Determine the outcome based on the number of differences
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution
do_main()


  1 2 3
  1 2 4
  

  1 2 3
  4 5 6
  