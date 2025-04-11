#BINARY SEARCH
def binary_search(list1,x,low,high):
    if low <=high:
        mid = low + (high - low) //2
        
        if list1[mid] == x:
            return mid
        elif list1[mid] < x:
            return binary_search(list1,0,low, mid - 1)
        else:
            return binary_search(list1, 0 , mid + 1,high)
        
    else:
        return - 1
    
list1 = [2,3,4,5,6,7,8]
x=5
result=binary_search(list1,x,0,len(list1)-1)
if result!= -1:
    print("Found At " +str(result))
else:
    print("not ")