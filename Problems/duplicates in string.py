str = "geeksforgeeks"
duplicates=[]
count=[]
for i in str:
  if str.count(i)>1:
      if i not in duplicates:
          duplicates.append(i)
print(*duplicates)

output:
  g e k s
