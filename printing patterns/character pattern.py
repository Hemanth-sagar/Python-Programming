n = int(input())
i = 1
while i<=n:
    j = 1
    # ord returns ASCII value of argument uh passed
    x = ord('A')
    while j <= i:
        #chr returns character of value --> chr(65)=='A'
        print(chr(x),end=" ")
        j=j+1
        x=x+1
    print()
    i = i+1
output:
 n = 4
A 
A B 
A B C 
A B C D 
