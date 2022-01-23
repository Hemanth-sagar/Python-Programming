'''
 Program to reverse a string with '.' 
 input:
   hello.hai.here
 output:
   here.hai.hello
'''

s = input()
x = s.split(".")
b=""
for i in range(len(x)-1,-1,-1):
    b=b+x[i]
    if i != 0:
        b=b+"."
print(b)
