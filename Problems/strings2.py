Given string of s and a number k.Print all the substring of s of length k
input:
  prog 
  2
output:
  pr ro og

s=input()
n=int(input())
l=[]
for i in range(len(s)+1):
  for j in range(i+1,len(s)+1):
    l.append(s[i:j])
for i in l:
    if len(i)==n:
        print(i,end=" ")
