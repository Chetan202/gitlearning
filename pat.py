def pattern(n):
    for i in range(1,n):
       for j in range(1,i+1):
           print("* ",end=' ')
       print("\r")
    for i in range(n,0,-1):
        for j in range(0,i):
            print("* ",end=' ')
        print("\r")
      
n=5
pattern(n)
print("In dev branch")
            
