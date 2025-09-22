def doMain():
    t1 = input()
    t2 = input()
    
    tt1 = t1.split()
    tt2 = t2.split()
    
    res = 0
    
    for x in range(3):
        a = int(tt1[x])
        b = int(tt2[x])
        
        if a != b:
            res += 1
    
    if res < 3:
        print("YES")
    else:
        print("NO")

doMain()


     1 2 3
     1 2 4
     

     5 6 7
     5 6 7
     

     1 2 3
     4 5 6
     

     2 3 4
     2 3 5
     

     0 1 2
     0 1
     