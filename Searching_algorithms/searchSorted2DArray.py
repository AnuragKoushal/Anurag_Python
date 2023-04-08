
# Function Definition
def SearchSorted2DArray(matrix, target):
    m = len(matrix)
    if m ==0:
        return False
    n= len(matrix[0])
    # Binary Search implementation
    left, right = 0, m*n-1
    while left<= right:
        mid = left + (right -left)//2
        # extracting middle value
        # row = indx//n
        # column = indx% n
        mid_element = matrix[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target< mid_element:
            right = mid -1
        else:
            left = mid + 1
    return False

# Driver code 
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

#function calling
result = SearchSorted2DArray(matrix, target)
print(result)