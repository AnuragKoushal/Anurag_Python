s= "aaabbbbcccddd"
target ="c"
ch ={}
for i in s:
    print(i)
    if i in ch:
        ch[i]=ch[i]+1
        #print(ch[i])
    else:
        ch[i] =1
result = ch[target]
print (result)