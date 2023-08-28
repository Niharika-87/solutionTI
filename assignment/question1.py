def fun(arr):
    s=[]
    for i in range(len(arr)):
        if arr[i] not in s:
            s.append(arr[i])
        else:
            pass 
    return s

arr=list(map(int,input().split()))
print(fun(arr))