def doMain():
    t1 = input()
    t2 = input()
    
    tt1 = t1.split()
    tt2 = t2.split()
    
    res = 0
    
    for index in range(3):
        a = int(tt1[index])
        b = int(tt2[index])
        
        if a != b:
            res += 1
    
    if res < 3:
        print("YES")
    else:
        print("NO")

doMain()
