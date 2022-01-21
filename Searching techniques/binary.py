def fun(li,x):
    l = 0
    r = len(li) - 1
    while l <= r:
        m = (l + r) // 2
        if li[m] == x:
            if x % 2 == 0:
                print("Yes - even")
            else:
                print("Yes - odd")
            break
        elif li[m] < x:
            l = m + 1
        else:
            r = m - 1
t=int(input())
li = list(map(int,input().split()))
x =[]
while t>0:
    a = int(input())
    x.append(a)
    t -= 1
for i in x:
    fun(li,i)
    
input:
  t = 4
1 2 3 4 5 6 
x:
  1
  2
  3
  4
output:
Yes - odd
Yes - even
Yes - odd
Yes - even
