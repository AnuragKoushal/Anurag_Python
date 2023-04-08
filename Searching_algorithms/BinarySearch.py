# Function Definition with recursion
# def BinarySearch(arr,i,j,x):
#     while i<=j:
#         mid = i+(j-i)//2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid]< x:
#             #recursion ==> calling the same function with different set of values
#             return BinarySearch(arr,mid+1,j,x)
#         else:
#             return BinarySearch(arr,i,mid-1,x)
#     return -1
 


## Driver Code
arr=[2, 5, 10, 14, 18, 22, 27, 35, 40, 59]
x= 40
i=0
j=len(arr)-1




# Function Definition without recursion
def BinarySearch(arr,i,j,x):
    while i<=j:
        mid = i+(j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]< x:
            #update the i parameter
            i = mid + 1
        else:
            #update the j parameter
            j= mid -1
            
    return -1





## Function Calling
result = BinarySearch(arr,i,j,x) 
print("Searching varible found at index", result)

