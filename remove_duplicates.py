### ARRAY is sorted


# driver code
arr = [1,1,3,3,4,5,6,6,6,8,8,10]
n = len(arr)
# Method definition

def sorted_array(arr,n):
    clean = []
    dup = []
    for i, el in enumerate (arr):
        if el not in clean:
            clean.append(el)
        else:
            dup.append(el)
    return clean,dup

# function calling
result = sorted_array(arr,n)
print("cleaned array", result[0]) 
print("duplicate reecords", result[1])



# def sorted_array(arr,n):
#     ans=[arr[0]]
#     for el in arr:
#         if ans[-1]!=el:
#             ans.append(el)
#     return print(ans)
