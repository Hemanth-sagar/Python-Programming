n = int(input())
i = 1
while i<=n:
    j = 1
    x = ord('A')
    while j <= i:
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
