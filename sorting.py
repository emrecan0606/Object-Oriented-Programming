def selection_sort(data):
    """return sorted copy of 'data' """
    array=data.copy()
    size =len(array)

    for i in range(size):
        #do something
        min_index=i
        
        #this for loop finds the minimum
        for j in range(i,size):
            
            if array[j]<array[min_index]:
                min_index=j
            #do something
                
        (array[i],array[min_index])=(array[min_index],array[i])   

    return array
#-----------------------------------------------------------------------
def bubble_sort(data):
    swapped=False
    
    array=data.copy()
    size=len(array)

    for i in range(size):
        for j in range(size-i-1):
            if array [j]>array[j+1]:
                #temp=array[j]
                #array[j]=array[j+1]
                #array[j+1]=temp
                (array[j],array[j+1])=(array[j+1],array[j])
                swapped=True
        if not swapped:
           break         
    return array  

#--------------------------------------------------------------------------------
def merge_sort(data):
    array=data.copy()
    size=len(array)

    if size >1:
        half=size//2
        left=array[:half]
        right=array[half:]
        
        print(f"Original {array}")
        merge_sort(left)
        merge_sort(right)

        print(f"after {array} ")

        i=j=k=0

       #combine them together

    while i<len(left) and j<len(right):
          if left[i]<=right[j]:
              array[k]=left[j]
              i=i+1
          else:
             array[k]=right[j]
             j=j+1
          k=k+1     





    while i<len(left):
        array[k]=right[j]
        j=j+1
        k=k+1

    while j<len(right):
        array[k]=right[j]
        j=j+1
        k=k+1

        return array  

import time

data=[9,-1,0,55,20]

t=[]
for i in  range(100):

   start=time.time()

   sorted_array=bubble_sort(data)

   # print("Function run took ",time.time()- start,"seconds")

   #t.append(time.time(0-start))



print("Average is",sum(t)/len(t),"seconds")

              





#testing area
#data=[9,-1,0,55,20]
#print(selection_sort(data))
#print(bubble_sort(data))
