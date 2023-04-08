# Driver code
arr = [70,20,50,30,90,5,15]
n= len(arr)


# Function Definition
def BubbleSort(arr):
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index = j
        #swap the element at i with min_index
        arr[i], arr[min_index] = arr[min_index], arr[i]    
    return arr

# Function Calling
result = BubbleSort(arr)
print(result)
