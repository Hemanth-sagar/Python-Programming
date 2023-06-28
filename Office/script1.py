line='''
this is
multiline
string '''
print(line)
line="""
this is
also
multiline"""
line="this is \nalso multi line \n using escape"

line=" double with in a \" string"
line=r'this/hel//jeh/'
line=[1,2,3]
line=[1,[2,3],3]
line=1 in line
line=[1,'rgd']
line=line+[100]
print(len(line))
line.append(9)
line.insert(3,33)
print(line.pop())
# line.clear()
print(line.index(33))
print(line.count(3))
line.sort()
print(line)


n1=int(input("first"))
n2=int(input("second"))
n3=int(input("third"))
if n1>n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
else:
    if n2>n3:
        print(n2)
    else:
        print(n3)

input_str=input()
print(input_str)

def vowels(str):
    count=0
    str=str.lower()
    for i in str:
        if i in ['a','e','i','o','u']:
            count+=1
    return count
string=input()
print("No of vowels: "+str(vowels(string)))

def cal(num1,num2,op):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '/':
        return num1/num2
    elif op == '%':
        return num1%num2
num1 = int(input())
num2 = int(input())
op = input()
 # , - ,* , /
print(cal(num1,num2,op))

char = input()
if char in ['a','e','i','o','u']:
    print("vowel")
else:
    print("not vowel")

num = int(input())
sum=1
while num>0:
    sum*=num
    num-=1
    # print(sum)
print(sum)

def sum_of_squ(num):
    s = str(num)
    sum=0
    for i in s:
        val = int(i)
        sum+=val*val
    return sum
num = int(input())
print(sum_of_squ(num))

0, 1, 1, 2, 3, 5, 8, 13, 21
def fib():
    first = 0
    second = 1
    print("0")
    print("1")
    sum =0
    while sum<50:
        sum = first+second
        if(sum>=50): break
        print(sum)
        first = second
        second = sum
fib()

str1 = input()
str2 = input()
str3=""
for i in range(len(str1)//2):
    str3+=str1[i]
str3+=str2
for i in range(len(str1)//2,len(str1)):
    str3+=str1[i]
print(str3)

str1 = input()
sum = 0
str1 = str1.split()
print(str1)
count = 0
for i in str1:
    if i.isdigit():
        print(i)
        sum+=int(i)
        # print(sum)
        count+=1
    # print()
print("sum is: "+str(sum))
print("avg is: "+str(sum/count))

My name is Sam I live in Mumbai
st = input()
st = st.split()
print(st)
st.reverse()
print(st)

st = input()
st = st.replace('.','')
st = st.split()
# print(st)
max=0
s=''
for i in st:
    # print(i)
    # print(st.count(i))
    if st.count(i)>max:
        max = st.count(i)
        # print(st.count(i))
        s = i
print(s+" is occuring "+str(max)+' times')

ls = [1,2,20,3,4,20]
print(ls.sort())
print(ls)
method1
for i in range(len(ls)):
    if ls[i]==20:
        ls[i]=200
        break
method2
print(ls)
if 20 in ls:
    index=ls.index(20)
    ls[index]=200
print(ls)


t = (('a', 23), ('b', 37), ('c', 11), ('d',29))

dict = {}
dict['a']=1
dict['b']=2
dict['c']=3
dict['d']=4
print(dict)
key = input("Enter key to delete")
dict.pop(key)
print(dict)
key1 = input("Enter key to search")
print(dict[key1])
print(dict.get(key1))
print(dict)


find = lambda x,y,z: min(x,y,z)
print(find(1,2,3))

str = input()
print(str[::-1])
print(str[::2])

import pandas as pd
list=[1,2,3,4,4,5,5,6,6,67,4]
df=pd.DataFrame(list)
print(df)

import pandas as pd
df=pd.read_csv("/home/ubuntu/Desktop/workspace/out.csv")
print(df)

import pandas as pd
df=pd.read_excel("/home/ubuntu/Desktop/Book1.xlsx")
print(df)

import pandas as pd
df=pd.read_excel("/home/ubuntu/Desktop/Employee Sample Data.xlsx")
print(df)

import pandas as pd
import sqlite3
con=sqlite3.connect("Demo.db")
cur = con.cursor()
# cur.execute("insert into Trainess values (2,'Srinivas',989988),(3,'Sushma',987788)")
con.commit()
cur.execute("Select * from Trainess")
cur.execute("desc Trainess")

data=cur.fetchall()
df=pd.DataFrame(data)
print(df)

import numpy as np
ls=np.array([[1,2,3,4],[5,6,7,8],[8,43,5,3]])
print(ls)
print(ls.flatten())
print(ls.T)
print(ls[1,0:3])
print(ls[2,:])
print(ls[:,2])
print(ls[1:,2])
newarr=np.ones(10)
print(newarr)
print(ls.reshape(3,4))
print(np.max(ls,axis=1))
print(np.min(ls,axis=1))
print(np.sum(ls,axis=1))
print(ls.dtype)
print(ls.shape)
print(ls.size)



Python database operation

1.Create  a table in database as student which has studentid , studentname and studentage as coloumns
2.Accept values from user and insert 5 record in student table.  
3Print all the data from student table
4.Accept a studentid from user and update studentname and studentage.
5.Accept a studentid from user and delete what record. 

import sqlite3
con = sqlite3.connect("Demo.db")
cur = con.cursor()
cur.execute("Drop table Student")
cur.execute("Create table Student(studentid,studentname,studentage)")
for i in range(3):
    id=int(input("enter id "))
    name=input("enter name")
    age=int(input("age"))
    cur.execute("insert into Student(studentid,studentname,studentage) values(?,?,?)",(id,name,age))
res=con.execute("select * from Student")
data=res.fetchall()
print(data)

id=int(input("enter id to update name and age"))
new_name=input("enter name")
new_age=int(input())
cur.execute("update Student set studentname=?,studentage=? where studentid =?",(new_name,new_age,id))
res=cur.execute("select * from Student")
data=res.fetchall()
print(data)

import matplotlib.pyplot as mt

mt.plot([1,4,6],[5,2,8])
mt.title("Plot1")
mt.xlabel("x-axis")
mt.ylabel("y-axis")
mt.show()
pie
labels=["A","B","C"]
mt.pie([25,25,50],labels=labels,colors=["Red","Green","Yellow"])
size=[25,25,50]
color=["Red","Green","LightPink"]
mt.pie(size,labels=labels,colors=color)
mt.show()
bar
x=["A","B","C","D"]
y=[5,3,4,9]
mt.bar(x,height=y,width=0.8)
mt.show()

exceltomatplotlib
import pandas as pd
import matplotlib.pyplot as mt
df=pd.read_excel("/home/ubuntu/Desktop/empdata_matplot.xlsx")
print(pd.DataFrame(df))
emp_names=df['Ename']
eage=df['Eage']
mt.bar(emp_names,height=eage,color=["red","green","blue","yellow","black"])
mt.show()
mt.pie(eage,labels=emp_names)
mt.show()










