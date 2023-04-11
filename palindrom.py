# ## driver code
# s = "NITIN"

# # method definition
# def palindrome(s):
#     rev_string = s[::-1]
#     if rev_string == s:
#         result = "yes"
        
#     else:
#         result = "no"
#     return result     
    
# # #function calling
# result = palindrome(s)
# print(result)

# #n = len(s)
n = 122
def palindrome_number(n):
    temp = n
    rev_number = 0
    while temp>0:
        digit = n % 10
        rev_number = rev_number*10 + digit
        temp = n //10
    if rev_number == n:
        print("palindrome") 
    else:
        print("no") 
     
           
#function calling
result = palindrome_number(n)
print(result)   