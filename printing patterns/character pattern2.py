n = int(input())
i = 1
while i<=n:
    j = 1
    x = ord('A')
    while j <= n:
        print(chr(x+j-1),end=" ")
        j=j+1
    print()
    i = i+1
output:
  n = 4
A B C D 
A B C D 
A B C D 
A B C D 
