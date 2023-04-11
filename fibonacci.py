def solve(n):
    a,b = 0,1
    print(a)    
    while (b < n ):
        print(b)
        a, b = b , a+b
        
solve(20)