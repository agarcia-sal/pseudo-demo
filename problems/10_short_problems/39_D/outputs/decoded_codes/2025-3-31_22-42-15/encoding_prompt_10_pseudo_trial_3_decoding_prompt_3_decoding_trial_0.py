def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a result counter
    res = 0
    
    # Compare elements from both lists
    for x in range(3):
        a = int(tt1[x])
        b = int(tt2[x])
        
        if a != b:
            res += 1
    
    # Determine the result based on the comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()


   1 2 3
   1 2 3
   

   1 2 3
   4 5 6
   

   1 2 3
   3 2 1
   