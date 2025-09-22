def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the two input strings by space into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    differences_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Check if the integers are different
        if a != b:
            # Increment the difference counter
            differences_count += 1

    # Check the number of differences
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    do_main()


  1 2 3
  1 2 4
  

  YES
  

  5 6 7
  5 6 7
  

  NO
  

  1 1 1
  2 2 2
  

  NO
  