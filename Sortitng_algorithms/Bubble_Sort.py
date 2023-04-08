# Driver code
arr = [70,20,50,30,90,5,15]
n= len(arr)


# Function Definition
def BubbleSort(arr):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:
                # Swap of element
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Function Calling
result = BubbleSort(arr)
print(result)