#pattern 2
'''
1
1 1
2 0 2
3 0 0 3
'''
n = int(input())
i = 1
p = 2
while i<= n:
    j = 1
    while j <= i:
        p = i - 1
        if i == 1 or i == 2:
            print("1 ",end="")
        elif j == 1 or j == i:
            print(p,end=" ")
        else:
            print("0 ",end="")
        j +=1
    i +=1
    print()

 # pattern 3
input:
    n = 4
output:
1 
1 1 
1 2 1 
1 2 2 1 

n = int(input())
i = 1
p = 2
while i<= n:
    j = 1
    while j <= i:
        p = i - 1
        if i == 1 or i == 2:
            print("1 ",end="")
        elif j == 1 or j == i:
            print("1",end=" ")
        else:
            print("2 ",end="")
        j +=1
    i +=1
    print()
