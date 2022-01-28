Statement:

Input will be like 5624381275. Separate odd places integers = 6, 4, 8, 2, 5

You have to return a 4-digit OTP by squaring the digits. Digits according to

input are 6, 4, 8, 2, 5

Square those numbers - 36, 16, 64, 4, 25

So, the OTP to be returned is first four digits i.e. 3616

#program
s = input()
l=[]
for i in range(1,len(s),2):
    l.append(int(s[i]))
sql=[number ** 2 for number in l]
f=""
for i in sql:
    f+=str(i)
for i in range(4):
    print(f[i],end="")

Input: 5624381275

Output: 3616
