# pattern 1
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

# pattern 2
n = int(input())
i = 1
while i<=n:
    j = 1
    x = ord('A') + i - 1
    while j <= n:
        print(chr(x+j-1),end=" ")
        j=j+1
    print()
    i = i+1
    
 input:
    n = 4
 output:
  
A B C D 
B C D E 
C D E F 
D E F G 

# pattern 3 
# intresting alphabets
n = int(input())
i = 1
while i <= n:
    j = 1
    x = ord('A') + n -1 # E
    while j<= i:
        print(chr(x - i + j),end=" ")
        j = j+1
    print()
    i = i +1
 input:
    n = 5
 output:  
E
D E
C D E
B C D E
A B C D E

# pattern 4
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
    
 input:
    n = 4
 output:
A B C D 
A B C D 
A B C D 
A B C D 
