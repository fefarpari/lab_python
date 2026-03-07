#len() number of element
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr))

#append() add element at end
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#insert(pos,x) insert at position
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#remove first occurrence
arr=array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)

#pop remove and return last element
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed : ",x)
print(arr)

#index find index of element
arr=array('i',[10,20,30,40])
print(arr.index(30))

#count occurrences
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#reverse array
arr=array('i',[40,30,20,10])
print(arr)
