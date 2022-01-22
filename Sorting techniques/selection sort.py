lst = list(map(int,input().split()))
#selection sort logic
for i in range(len(lst)):
  min = i
  
  #finding minimum
  for j in range(i+1,len(lst)):
    if lst[min] > lst[j]:
      min = j
      
  #swapping elements after finding
  lst[i],lst[min]=lst[min],lst[i]
print("Sorted List ",lst)
