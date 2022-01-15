#pattern 1
r = int(input())
c = int(input())
i = 1
while i <= r:
    j = 1
    while j <= c:
        if i == 1 or i == r:
            print("*", end="")
        elif j == 1 or j == c:
            print("*", end="")
        elif j != 1 or j != c:
            print(" ", end="")
        j = j + 1
    i = i + 1
    print()
    
  input :
    r = 3
    c = 6
  output:
    
******
*    *
******
